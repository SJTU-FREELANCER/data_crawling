# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Wuba1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Rec_Title = scrapy.Field()
    Rec_Salary = scrapy.Field()
    Tags = scrapy.Field()
    Company = scrapy.Field()
    Rec_Cate = scrapy.Field()
    Rec_Education = scrapy.Field()
    Rec_Experience = scrapy.Field()
    Rec_Location = scrapy.Field()
    
