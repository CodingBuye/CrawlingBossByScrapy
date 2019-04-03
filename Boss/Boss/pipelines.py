# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from Boss.settings import mongo_host, mongo_port, mongo_db_name, mongo_db_connection


class BossPipeline(object):

    def __init__(self):
        host = mongo_host
        port = mongo_port
        dbname = mongo_db_name
        tablename = mongo_db_connection
        client = pymongo.MongoClient(host=host, port=port)
        my_database = client[dbname]
        self.post = my_database[tablename]

    def process_item(self, item, spider):
        """
        :param item: boss_spider中yield过来的boss_item
        :param spider:
        :return:
        """
        data = dict(item)
        self.post.insert(data)
        return item
