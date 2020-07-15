import scrapy
from ..items import Wuba1Item


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['58.com']
    # 配置起始页url
    offset = 1
    url = "https://sz.58.com/job/pn{0}/"
    start_urls = [url.format(str(offset))]

    def parse(self, response):
        for each in response.xpath("//ul[@id='list_con']/li"):
             item = Wuba1Item()
            item['Rec_Title'] = each.xpath(".//span[@class='name']/text()").extract()[0]
            money_list = each.xpath(".//p[@class='job_salary']/text()").extract()
            money = "未知"
            if len(money_list) > 0:
                money = money_list[0]
            item['Rec_Salary'] = money
            span = each.xpath(".//div[@class='job_wel clearfix']/span")
           
            item['Tags'] = ""
            for i in span:
                item['Tags']= item['Tags'] + "  " + i.xpath("./text()").extract()[0]              
            item['Company'] = each.xpath(".//div[@class='comp_name']/a/text()").extract()[0]
            item['Rec_Cate'] = each.xpath(".//span[@class='cate']/text()").extract()[0]
            item['Rec_Education'] = each.xpath(".//span[@class='xueli']/text()").extract()[0]
            item['Rec_Experience'] = each.xpath(".//span[@class='jingyan']/text()").extract()[0]
            item['Rec_Location'] = "深圳， "+each.xpath("//span[@class='address']/text()").extract()[0]
            yield item
        if self.offset < 100:
            self.offset += 1
        yield scrapy.Request("https://sz.58.com/job/pn{0}/".format(str(self.offset)), callback=self.parse)
           
            