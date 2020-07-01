import logging
from wukong.kafka.producer import Producer

logger = logging.getLogger(__name__)

class DataSource:
    def __init__(self, cfg):
        self.cfg_ = cfg
        self.__create_producer()

    def __create_producer(self):
        self.producer_ = Producer(self.cfg_)

    def generate_message(self):
        assert(False)

    def run(self):
        for msg in self.generate_message():
            self.producer_.send(msg)

