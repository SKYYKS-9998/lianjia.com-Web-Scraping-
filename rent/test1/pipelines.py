# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import csv

# 输出csv文件
class MyPipeline(object):
    def open_spider(self, spider):
        try:
            self.file = open("quanzhou.csv", 'a', newline='', encoding="utf-8")
        except Exception as err:
            print(err)

    def process_item(self, item, spider):
        list_item = [item['rent'], item['block'], item['area'], item['direction'], item['room']]
        f_csv = csv.writer(self.file)
        f_csv.writerow(list_item)
        return item

    def close_spider(self, spider):
        self.file.close()
