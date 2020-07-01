import logging
import psycopg2

logger = logging.getLogger(__name__)

class PostgresDB:
    def __init__(self, default_uri, cfg):
        self.default_uri_ = default_uri
        self.cfg_ = cfg
        self.conn_ = None

    def connect(self, default=False):
        try:
            if default:
                self.conn_ = psycopg2.connect(self.default_uri_)
            else:
                self.conn_ = psycopg2.connect(**self.cfg_)
            self.conn_.autocommit = True
            cur = self.conn_.cursor()
            cur.execute('SELECT version()')
            db_version = cur.fetchone()
            # display the PostgreSQL database server version
            logger.info('PostgreSQL database version: %s', db_version)
            cur.close()
            return True
        except (Exception, psycopg2.DatabaseError) as e:
            logger.fatal("Failed to connect postgres: ", e)
        return False

    def __db_exists(self, db_name):
        cur = self.conn_.cursor()
        cur.execute("SELECT datname FROM pg_database;")
        databases = cur.fetchall()
        return (db_name,) in databases

    def create_db_if_not_exists(self, db_name):
        if self.connect(default=True):
            if not self.__db_exists(db_name):
                self.execute("CREATE DATABASE " + db_name, {})
            self.close()

    def execute(self, sql, params):
        try:
            cur = self.conn_.cursor()
            cur.execute(sql, params)
            return True
        except Exception as e:
            logger.error(f"Failed to execute {sql}", e)
        return False

    def close(self):
        self.conn_.close()
