import logging
import yaml

logger = logging.getLogger(__name__)

class Config:
    def __init__(self, root, cfgfile):
        self.root_ = root
        with open(root + '/' + cfgfile) as cfile:
            self.cfg_ = yaml.load(cfile, Loader=yaml.FullLoader)

    @property
    def api_version(self):
        return self.cfg_['api_version']

    @property
    def topic(self):
        return self.cfg_['topic']

    @property
    def auto_offset_reset(self):
        return self.cfg_['auto_offset_reset']

    @property
    def bootstrap_servers(self):
        return self.cfg_['bootstrap_servers']

    @property
    def security_protocol(self):
        return self.cfg_['security_protocol']

    @property
    def ssl_cafile(self):
        return self.root_ + '/' + self.cfg_['ssl_cafile']

    @property
    def ssl_certfile(self):
        return self.root_ + '/' + self.cfg_['ssl_certfile']

    @property
    def ssl_keyfile(self):
        return self.root_ + '/' + self.cfg_['ssl_keyfile']

    @property
    def client_id(self):
        return self.cfg_['client_id']

    @property
    def group_id(self):
        return self.cfg_['group_id']

    @property
    def enable_auto_commit(self):
        return self.cfg_['enable_auto_commit']