import scrapy
from ..items import Wuba1Item


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['58.com']
    # 配置起始页url
    offset = 1
    url = "https://sh.58.com/job/pn{0}/"
    start_urls = [url.format(str(offset))]

    #解析html内容
    def parse(self, response):
        for each in response.xpath("//ul[@id='list_con']/li"):
            item = Wuba1Item()
            item['job_name'] = each.xpath(".//span[@class='name']/text()").extract()[0]
            money_list = each.xpath(".//p[@class='job_salary']/text()").extract()
            money = "未知"
            if len(money_list) > 0:
                money = money_list[0]
            item['money'] = money
            span = each.xpath(".//div[@class='job_wel clearfix']/span")
            item['job_wel'] = []
            for i in span:
                item['job_wel'].append(i.xpath("./text()").extract()[0])
            item['company'] = each.xpath(".//div[@class='comp_name']/a/text()").extract()[0]
            item['position_type'] = each.xpath(".//span[@class='cate']/text()").extract()[0]
            item['xueli'] = each.xpath(".//span[@class='xueli']/text()").extract()[0]
            item['jingyan'] = each.xpath(".//span[@class='jingyan']/text()").extract()[0]
            item['address'] = each.xpath("//span[@class='address']/text()").extract()[0]
            yield item
        if self.offset < 100:
            self.offset += 1
        yield scrapy.Request("https://sh.58.com/job/pn{0}/".format(str(self.offset)), callback=self.parse)