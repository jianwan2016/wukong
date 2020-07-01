import logging
from kafka import KafkaConsumer

logger = logging.getLogger(__name__)

class Consumer:
    def __init__(self, cfg):
        self.cfg_ = cfg
        self.__create_consumer()

    def __create_consumer(self):
        self.consumer_ = KafkaConsumer(self.cfg_.topic,
                                       auto_offset_reset=self.cfg_.auto_offset_reset,
                                       bootstrap_servers=self.cfg_.bootstrap_servers,
                                       client_id=self.cfg_.client_id,
                                       group_id=self.cfg_.group_id,
                                       api_version=self.cfg_.api_version,
                                       enable_auto_commit=self.cfg_.enable_auto_commit,
                                       security_protocol=self.cfg_.security_protocol,
                                       ssl_cafile=self.cfg_.ssl_cafile,
                                       ssl_certfile=self.cfg_.ssl_certfile,
                                       ssl_keyfile=self.cfg_.ssl_keyfile)

    def consume(self):
        while True:
            try:
                for msg in self.consumer_:
                    yield msg
            except Exception as e:
                logger.fatal("Failed to consume message:", e)
                if self.consumer_ is not None:
                    self.__create_consumer()
                else:
                    logger.fatal("Kafka service is gone? exiting")
                    raise e

