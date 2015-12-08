# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class YuncaijingNewsPipeline(object):
    def __init__(self):
        self.file = open('items.json', 'wb')

    def process_item(self, item, spider):
        file_obj = open('./ycj_news/' + item['No'] + '.ycj', 'wb')
        line = json.dumps(dict(item), ensure_ascii=False)
        file_obj.write(line.encode('utf-8'))
        file_obj.close()
        return item
