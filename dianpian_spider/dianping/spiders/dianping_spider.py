# coding=utf-8

import scrapy
from scrapy import Request
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
    allowed_domains = ["www.dianping.com"]
    start_urls = [
        # "http://www.dianping.com/shop/98912242",
        "http://www.dianping.com/",
    ]
    handle_httpstatus_list = [301, 403]

    # rules = {
    #     Rule(LinkExtractor(allow=r'2003\/12\/[\/_\w]*.html'), callback='parse_item'),
    #     Rule(LinkExtractor(allow=r'2003\/12'), follow=True)
    # }

    # def make_requests_from_url(self, url):
    #     print '------------------------------------'
    #     print url
    #     print '------------------------------------'

    #     return Request(url, meta={'handle_http_status_list': [301, 403]}, callback=self.parse_item)

    # def parse_item(self, response):
    def parse(self, response):

        print sys.stdout.encoding

        print sys.getdefaultencoding()
        for sel in response.css('article'):
            item = DianpingItem()
            # item['titleCSSSelector'] = sel.css('a').select('@href').extract_first()
            item['title'] = sel.xpath('h1/text()').extract_first()
            item['link'] = ''  # sel.xpath('a/@href').extract_first()
            item['desc'] = ''  # sel.xpath('text()').extract_first()
            yield item
