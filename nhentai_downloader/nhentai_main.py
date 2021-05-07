#!/usr/bin/env python
# coding:utf-8
"""
# NHentai Scripts
# Author: Karonheaven
"""
# +---------------+需要的包+---------------+
# 标准库导入
from typing import *
import logging
import os
import time
import datetime
from threading import Thread
from queue import Queue

# 第三方库导入
import requests


# 本地库/自定义库导入


# +---------------+全局变量&预定义+---------------+
def get_time_dif(start_time):
    """
    获取总运行时间(通过计算时间差)
    
    :param start_time: 起始时间
    :return: 运行时间
    """
    end_time = time.time()
    time_dif = end_time - start_time
    return datetime.timedelta(seconds=int(round(time_dif)))


def join_url(nh_id: str) -> str:
    """
    根据NH ID拼接URL
    
    :param book_id: NH ID
    :return: 拼接后的URL
    """
    # 检查NH ID的数据类型
    if not isinstance(nh_id, str):
        logging.warning("NHentai ID数据类型错误: {}".format(nh_id))
    
    # 进行URL拼接
    _url = "https://nhentai.net/g/{}/".format(nh_id)
    
    return _url


"""
转换评论格式
    输入：NH ID(不确定语言)

    1. 构建Dict，填入以下数据：
        →raw_id: 原始NH ID
        →raw_url: 原始NH URL
    2. 将Dict填入Info Queue中
    =====Info Queue=====
    3. 从Info Queue中取出一个Info Dict
    4. 判断URL的连通性



    1. 判断NH ID是否存在
    2. 若NH ID存在，构造Info Dict，否则返回错误
    3. 根据原始NH ID，查询并将以下信息填入到字典中：


        →lang_raw: 原始本子语言
        →book_name_jp: 原始NH ID对应的本子日文名
        →book_name_raw: 原始NH ID对应的本子英文名
    4. 将该Info Dict填入到Search Queue中

    =====Search Queue======
    5.



"""


class NHentaiModuleMultiThread():
    """
    检索&下载模块
    """
    
    def __init__(self, thread_num: int = 1):
        """
        初始化模块

        :param thread_num: 多线程的线程数
        """
        # 等待列表，做成队列形式
        # Get Info Queue: Queue[Dict]
        self.info_queue: Queue = Queue()
        # Search Queue: Queue[Dict]
        self.search_queue: Queue = Queue()
        # Download Queue: Queue[Dict]
        self.download_queue: Queue = Queue()
        
        # 保存文件夹
        self.save_dir: str = ""
        
        # URL
        self.url: str = ""
        
        # 线程数
        self.thread_num = thread_num
    
    def add_search_id(self, book_id: int) -> None:
        """
        向模块中添加一个ID

        :param book_id: ID
        :return: None，向待解析队列中添加节点
        """
        if not isinstance(book_id, str):
            logging.warning("输入的ID为int类型，请转换为str类型")
            book_id = str(book_id)
        
        # 构建Info Dict
        book_info_dict: Dict[str, str] = {}
        book_info_dict["raw_id"] = book_id
        book_info_dict["raw_url"] = join_url(nh_id=book_id)
        
        # 向Info Queue中填入Info Dict
        self.info_queue.put(book_info_dict)
        
        logging.info("Book: {}, 填入Info Queue完成")
        
        return None
    
    def _search(self, ):
    
    
    def search(name: str, lan: str) ->:
        return None
    
    pass


# +---------------+主程序+---------------+
pass
