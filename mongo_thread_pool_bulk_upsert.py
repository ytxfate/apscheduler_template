#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  mongo_thread_pool_bulk_upsert.py  
@Desc :  线程池批量更新MongoDB数据
'''

# Standard library imports
from typing import Generator
from concurrent.futures.thread import ThreadPoolExecutor
# from queue import Queue
# Third party imports
from pymongo import UpdateOne
from pymongo.database import Database
# Local application imports



def __bulk_upsert_one(db_mongo, coll_name, mutl_task, ordered=True):
    db_mongo[coll_name].bulk_write(mutl_task, ordered=ordered)


def mongo_thread_pool_bulk_upsert(
    upsert_datas: Generator,
    update_keys: list,
    db_mongo: Database,
    coll_name: str,
    max_workers: int=5,
    ordered: bool=True
):
    """线程池批量更新MongoDB数据
    建议使用线程池, PyMongo 是线程安全的
    
    @Params:
        upsert_datas    : 需要更新的数据, 建议使用生成器
        update_keys     : 按哪些字段去重更新
        db_mongo        : pymongo.database.Database
        coll_name       : 需要更新的表名
        max_workers     : 最大线程池数量, 默认 5
        ordered         : 是否按顺序执行 (经测试影响不大)
    """
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        upsert_list = []
        for usd in upsert_datas:
            us_obj = dict([(k, usd[k]) for k in update_keys])
            upsert_list.append(UpdateOne(filter=us_obj, update={'$set': usd}, upsert=True))
            if len(upsert_list) >= 500:
                pool.submit(__bulk_upsert_one, db_mongo, coll_name, upsert_list, ordered)
                upsert_list = []
        if upsert_list:
            pool.submit(__bulk_upsert_one, db_mongo, coll_name, upsert_list, ordered)
            upsert_list = []
