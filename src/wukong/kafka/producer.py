import logging
from kafka import KafkaProducer

logger = logging.getLogger(__name__)

class Producer:
    def __init__(self, cfg):
        self.cfg_ = cfg
        try:
            self.producer_ = KafkaProducer(bootstrap_servers=self.cfg_.bootstrap_servers,
                                           security_protocol=self.cfg_.security_protocol,
                                           ssl_cafile=self.cfg_.ssl_cafile,
                                           ssl_certfile=self.cfg_.ssl_certfile,
                                           ssl_keyfile=self.cfg_.ssl_keyfile)
        except Exception as e:
            logger.fatal("Failed to create kafka producer", e)
            raise e

    def send(self, pbmsg):
        logger.debug("Sending message: %s", pbmsg)
        self.producer_.send(self.cfg_.topic, value=pbmsg).get()
