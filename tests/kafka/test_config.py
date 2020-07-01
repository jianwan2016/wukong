# -*- coding: utf-8 -*-

import pytest
from wukong.kafka.config import Config

__author__ = "Jian Wan"
__copyright__ = "Jian Wan"
__license__ = "mit"


def test_config():
    cfg = Config('kafka', 'kafka.yaml')
    assert cfg.bootstrap_servers == 'bootstrap_server'
