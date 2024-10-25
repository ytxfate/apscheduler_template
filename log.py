#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  log.py  
@Desc :  日志
'''

# Standard library imports
import logging
from logging import handlers
# Third party imports
# Local application imports


logger = logging.getLogger()

logger.setLevel(level=logging.DEBUG)

formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | %(name)s:%(filename)s:%(lineno)-5d - %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)

time_rotating_file_handler = handlers.TimedRotatingFileHandler(filename='out.log', when='D')
time_rotating_file_handler.setLevel(logging.DEBUG)
time_rotating_file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(time_rotating_file_handler)


logger.debug('debug级别，一般用来打印一些调试信息，级别最低')
logger.info('info级别，一般用来打印一些正常的操作信息')
logger.warning('waring级别，一般用来打印警告信息')
logger.error('error级别，一般用来打印一些错误信息')
logger.critical('critical级别，一般用来打印一些致命的错误信息，等级最高')
