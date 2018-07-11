# coding=utf-8

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import sys
import logging
import dianping
from dianping.items import DianpingItem

reload(sys)
sys.setdefaultencoding('utf-8')


class DianpingSpider(CrawlSpider):
    name = "dianping"
    allowed_domains = ["www.ruanyifeng.com"]
    start_urls = [
        "http://www.ruanyifeng.com/blog/2004/01/",
    ]
    rules={
        Rule(LinkExtractor(allow='http://www.ruanyifeng.com/blog/2003/12/'), callback='parse_item')
        # ,
        # Rule(LinkExtractor(allow='/2013/', restrict_css="ul li"), callback='parse_item')
    }


    def parse_item(self, response):

        print sys.stdout.encoding

        print sys.getdefaultencoding()
        for sel in response.css('ul li'):

            # title = sel.xpath('a/text()').extract_first()
            # link = sel.xpath('a/@href').extract_first()
            # desc = sel.xpath('text()').extract_first()
            # logging.basicConfig(filename='f:/example.log', level=logging.DEBUG)
            # logging.debug('111')
            # logging.debug(title)
            # logging.debug(link)
            # logging.debug(desc)
            # print '------------------------------------------------------'
            # print desc
            # print link
            # print title
            # print '------------------------------------------------------'

            # filename = response.url.split("/")[-2]
            # with open(filename, "wb") as f:
            #     f.write(response.body)

            item = DianpingItem()
            item['titleCSSSelector'] = sel.css('a').select('@href').extract_first()
            item['title'] = sel.xpath('a/text()').extract_first()
            item['link'] = sel.xpath('a/@href').extract_first()
            item['desc'] = sel.xpath('text()').extract_first()
            yield item
