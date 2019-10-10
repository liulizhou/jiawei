# -*- coding: utf-8 -*-
import warnings
warnings.filterwarnings("ignore")
import os

from os import listdir
from os.path import join
import json

default_config = {}


override_config = {
    'ENV_TYPE': 'TEST',
    'WORKING_DIR': '/data/home/user00/shield/',
    'SPLIT_SYMBOL': '|',
    'TRANS_SWITCH_NAME': True,
    'TRANS_SWITCH_PINYIN': False,
    'TRANS_SWITCH_PINYIN_WITH_TONE': False,
    'MATCH_SWITCH_SUBSTRING_NAME': True,
    'MATCH_SWITCH_COMMONSTRING': True,
    'WORK_MODE': 'NAMELIST',
    'LOCAL_UDF_DATA_DIR': {
        'xumiaochun': '/Users/xumiaochun/python_workspace/southern_power_grid/data/multiple',
        'shihuanzhao': '/Volumes/shihuan/tencent-data/modelflow-data-online-5min/',
        'shuiliantan': '/Users/shuiliantan/tencent_work/2019aiopsdata/2019AIOps_data_test2'
    }}


class Config_json():
    def __init__(self, biz_id='DEFAULT', case_type='DEFAULT'):
        self.biz_id = biz_id
        self.case_type = case_type
        self.default_config = default_config
        self.override_config = override_config
        self.final_config = dict()
        self.final_config.update(self.default_config)
        self.final_config.update(self.override_config)
        self.final_config.update({'BIZ_ID': self.biz_id, 'CASE_TYPE': self.case_type})

    def get_config(self, value):
        try:
            res = self.final_config[value]
        except:
            res = None
        return res



def get_user_data_dir():
    config_json = Config_json()
    if os.getcwd().startswith('/Users/xumiaochun'):
        LOCAL_UDF_DATA_DIR = config_json.get_config('LOCAL_UDF_DATA_DIR')['xumiaochun']
    elif os.getcwd().startswith('/Users/stellazhao'):
        LOCAL_UDF_DATA_DIR = config_json.get_config('LOCAL_UDF_DATA_DIR')['shihuanzhao']
    elif os.getcwd().startswith('/Users/shuiliantan'):
        LOCAL_UDF_DATA_DIR = config_json.get_config('LOCAL_UDF_DATA_DIR')['shuiliantan']

    elif os.getcwd().startswith('/data/mapleleaf'):
        LOCAL_UDF_DATA_DIR = config_json.get_config('REMOTE_DATA_DIR')
    else:
        print('get_user_data_dir error ')
        LOCAL_UDF_DATA_DIR = ''
    print('your local data dir prefix is: %s' % (LOCAL_UDF_DATA_DIR))
    return LOCAL_UDF_DATA_DIR
