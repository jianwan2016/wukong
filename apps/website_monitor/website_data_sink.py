import sys
import time
import logging
import yaml

sys.path.append('../../src/')
sys.path.append('./message')

import wukong.kafka.config as kc
import wukong.sink.data_sink as ds
import wukong.postgres.postgres_db as postgres
import message.website_status_pb2 as pb

logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)

SERVICE_NAME = 'website_monitor'

class PostgresDBSink:
    def __init__(self, client_id, db_cfg):
        self.client_id_ = client_id
        self.dbcfg_ = db_cfg
        self.default_uri_ = db_cfg['uri'] # use for connection default
        del db_cfg['uri']
        self.__create()

    def __create(self):
        self.postgres_ = postgres.PostgresDB(self.default_uri_, self.dbcfg_)
        self.postgres_.create_db_if_not_exists(SERVICE_NAME)
        self.postgres_.connect()
        # The sql should be consistent with website_status.proto
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS status (
            timestamp BIGINT DEFAULT 0,
            monitor_id VARCHAR(32) NOT NULL,
            website VARCHAR(64) NOT NULL,
            response_time INTEGER DEFAULT 0,
            status_code INTEGER)
        """
        self.postgres_.execute(create_table_sql, {})

    def writeToDB(self, msg):
        insert_table_sql = """
        INSERT INTO status (timestamp, monitor_id, website, response_time, status_code)
        VALUES (%s, %s, %s, %s, %s)
        """
        if not self.postgres_.execute(insert_table_sql,
                (msg.base.timestamp, msg.monitor_id, msg.website, msg.response_time, msg.status_code)):
            logger.error("Failed to write %s", msg)

class WebsiteDataSink(ds.DataSink):
    def __init__(self, kafka_cfg, db_cfg):
        super().__init__(kafka_cfg)
        self.dbsink_ = PostgresDBSink(kafka_cfg.client_id, db_cfg)

    def sink_message(self, pbmsg):
        msg = pb.website_status()
        msg.ParseFromString(pbmsg)
        assert(msg.base.service_name == SERVICE_NAME)
        print(msg)
        self.dbsink_.writeToDB(msg)

def run():
    root_config_dir = 'config'
    kafka_cfg = kc.Config(root_config_dir, 'kafka.yaml')
    with open('config/postgres.yaml') as f:
        db_cfg = yaml.load(f, Loader=yaml.FullLoader)
    WebsiteDataSink(kafka_cfg, db_cfg).run()

if __name__  == '__main__':
    run()
