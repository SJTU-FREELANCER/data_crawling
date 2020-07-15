# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Wuba1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_name = scrapy.Field()
    money = scrapy.Field()
    job_wel = scrapy.Field()
    company = scrapy.Field()
    position_type = scrapy.Field()
    xueli = scrapy.Field()
    jingyan = scrapy.Field()
    address = scrapy.Field()
    
