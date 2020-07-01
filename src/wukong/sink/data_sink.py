import logging
from wukong.kafka.consumer import Consumer

logger = logging.getLogger(__name__)

class DataSink:
    def __init__(self, cfg):
        self.cfg_ = cfg;
        self.__create_consumer()

    def __create_consumer(self):
        self.consumer_ = Consumer(self.cfg_)

    def __consume_message(self):
        return self.consumer_.consume()

    def sink_message(self, pbmsg):
        pass

    def run(self):
        for msg in self.__consume_message():
            self.sink_message(msg.value)

