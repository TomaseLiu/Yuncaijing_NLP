#!/usr/bin/env python
#coding=utf-8
import scrapy
import re
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy.http import HtmlResponse

class News(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    time_source = scrapy.Field()
    related_industry = scrapy.Field()
    related_theme = scrapy.Field() 
    body = scrapy.Field()
    No = scrapy.Field()

class gainianguSpider(CrawlSpider):
    name = "YThemeNews"
    allowed_domains = ["www.yunvs.com/"]
    url = "http://yunvs.com/news/n6_%d_1.html"
    # [2570000, 3900000]
    start_urls = [url % i for i in range(2571780, 3900000)]
    #start_urls = [url % i for i in range(3000000, 3100000)]
    #start_urls = [url % i for i in range(3100000, 3150000)]
    #start_urls = [url % i for i in rang
    #start_urls = [url % i for i in range(2661111, 2661120)]

    def parse(self, response):
        response = HtmlResponse(url=response.url, status=response.status, headers=response.headers, body=response.body)
        url = response.url
        title = " ".join(response.xpath('/html/body/div[@class="container"]/div[@class="bodybox"]/div[1]/div[2]/h1/text()').extract())
        header = response.xpath('/html/body/div[@class="container"]/div[@class="bodybox"]/div[1]/div[2]/h2/text()').extract()
        if len(header) <= 1:
            return

        paragraph_list = response.xpath('/html/body/div[@class="container"]/div[@class="bodybox"]/div[1]/div[2]/div[2]/p/text()').extract()
        body = '\n'.join(paragraph_list)

        time_source = header[0]
        related_industry = ""
        related_theme = ""
        
        ri_key = "关联行业"
        rt_key = "关联概念"


        for item in header:
            print item
            if ri_key.decode('utf-8') in item:
                related_industry =  item.split(u'：')[1]
                #continue
            if rt_key.decode('utf-8') in item:
                related_theme = item.split(u'：')[1]

        if related_theme == "":
            return        

        file_name = './ycj_news/' + url.split('_')[1] + '.ycj'
        #print url, title, related_theme, body       

        news = News()
        news['title'] = title
        news['url'] = url
        news['time_source'] = time_source
        news['related_industry'] = related_industry
        news['related_theme'] = related_theme
        news['body'] = body
        news['No'] = url.split('_')[1]
        return news
        #self.write_news_into_file(file_name, url, title, time_source, related_industry, related_theme, body)
        
    def write_news_into_file(self, file_name, url, title, time_source, related_industry, related_theme, body):
        file_obj = open(file_name, 'w')
        file_obj.write('<title>' + title.encode('utf-8') + '</title>\n')
        file_obj.write('<url>' + url + '</url>\n')
        file_obj.write('<time_source>' + time_source.encode('utf-8') + '</time_source>\n')
        file_obj.write('<related_industry>' + related_industry.encode('utf-8') + '</related_industry>\n')
        file_obj.write('<related_theme>' + related_theme.encode('utf-8') + '</related_theme>\n')
        file_obj.write('<body>\n' + body.encode('utf-8') + '\n</body>')
