# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class DoubanPipeline(object):
#     def process_item(self, item, spider):
#         return item
import MySQLdb
from douban import settings
from douban.config import from_object

class MysqlPipeline(object):
    '''数据库操作'''
    middle = from_object(settings)
    def __init__(self):
        self.con = MySQLdb.connect(self.middle["host"],self.middle["user"],self.middle["password"],self.middle["db_name"],charset=self.middle["charset"],use_unicode = True)
        self.cursor = self.con.cursor()
    def process_item(self,item,spider):
        insert_sql = '''
                    INSERT INTO movie(rate,title,cover,playable) VALUES (%s,%s,%s,%s)
        '''
        self.cursor.execute(insert_sql,(item["rate"],item["title"],item["cover"],item["playable"]))

        self.con.commit()