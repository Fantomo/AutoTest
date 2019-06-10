# -*- encoding:utf-8 -*-
"""
公共配置
"""
import os
from .file_reader import YamlReader

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.yml')
UTILS_PATH = os.path.join(BASE_PATH, 'utils')
DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')
REPORT_PATH = os.path.join(BASE_PATH, 'report')
LOG_PATH = os.path.join(BASE_PATH, 'log')
DATA_PATH = os.path.join(BASE_PATH, 'data')


class Config:

	def __init__(self, config=CONFIG_FILE):
		self.config = YamlReader(config).data

	def get(self, element, index=0):
		return self.config[index].get(element)
