# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 五个项分别对应租金、板块、面积、朝向、居数
class Myitem(scrapy.item.Item):
    rent = scrapy.Field()
    block = scrapy.Field()
    area = scrapy.Field()
    direction = scrapy.Field()
    room = scrapy.Field()
