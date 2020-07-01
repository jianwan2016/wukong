import sys
import time
import logging
import requests

sys.path.append('../../src/')
sys.path.append('./message')

import wukong.kafka.config as kc
import wukong.source.data_source as ds
import message.website_status_pb2 as pb

logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)

SERVICE_NAME = 'website_monitor'

class WebsiteMonitor:
    def __init__(self, website):
        https = 'https://'
        if website.startswith(https):
            self.website_ = website
        else:
            self.website_ = https + website
    
    def check_status(self):
        start = int(round(time.time() * 1000))
        r = requests.get(self.website_)
        duration = int(round(time.time() * 1000)) - start
        return r.status_code, start, duration


class WebsiteDataSource(ds.DataSource):
    def __init__(self, kafka_cfg, website_cfg):
        self.client_id_ = kafka_cfg.client_id
        super().__init__(kafka_cfg)

    def generate_message(self):
        website = 'aiven.io' # hardcode for the moment, should be able to configure
        wm = WebsiteMonitor(website)
        while True:
            status_code, timestamp, response_time = wm.check_status()
            msg = pb.website_status()
            msg.base.service_name = SERVICE_NAME
            msg.base.timestamp = timestamp
            msg.monitor_id = self.client_id_
            msg.website = website
            msg.response_time = response_time
            msg.status_code = status_code
            time.sleep(1)
            yield msg.SerializeToString()

def run():
    root_config_dir = 'config'
    kafka_cfg = kc.Config(root_config_dir, 'kafka.yaml')
    logger.info("Loaded kafka config %s", kafka_cfg.cfg_)
    WebsiteDataSource(kafka_cfg, None).run()

if __name__  == '__main__':
    run()
