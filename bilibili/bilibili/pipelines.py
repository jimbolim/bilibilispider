# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymysql
from scrapy.utils.project import get_project_settings


class BilibiliPipeline(object):
    def process_item(self, item, spider):
        return item


class DBPipeline(object):
    def __init__(self):
        settings = get_project_settings()
        self.host = settings['MYSQL_HOST']
        self.user = settings['MYSQL_USER']
        self.pwd = settings['MYSQL_PASSWD']
        self.name = settings['MYSQL_DBNAME']
        self.charset = settings['MYSQL_CHARSET']
        self.connect()


    def connect(self):
        self.conn = pymysql.connect(host=self.host,
                             port=3306,
                             user=self.user,
                             password=self.pwd,
                             db=self.name,
                             charset=self.charset,
                             autocommit=True)
        self.cursor = self.conn.cursor()


    def close_spider(self, spider):
        self.conn.close()
        self.cursor.close()


    def process_item(self, item, spider):
        try:
            #(aid, view, danmaku, reply, favorite, coin, share, now_rank, his_rank, like, dislike, no_reprint, copyright)
            sql = "INSERT INTO video_information VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                item['aid'],item['view'],item['danmaku'],item['reply'],item['favorite'],item['coin'],item['share'],item['his_rank'],item['like'])
            # item['now_rank'],, item['dislike'], item['no_reprint'], item['copyright']
            self.cursor.execute(sql)

        except Exception as error:
            # 出现错误时打印错误信息
            print(error)
        return item
