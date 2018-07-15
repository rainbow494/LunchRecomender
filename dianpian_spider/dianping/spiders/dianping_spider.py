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
    allowed_domains = ["dianping.com"]
    start_urls = [
        # "http://www.dianping.com/shop/98912242",
        "http://dianping.com/",
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


        if (('Location' in response.headers) and (response.headers['Location'] != response.request.url)):
            yield scrapy.Request(url=response.headers['Location'], callback=self.parse)
            return
        else:
            from scrapy.shell import inspect_response
            inspect_response(response, self)

        print sys.stdout.encoding

        print sys.getdefaultencoding()
        for sel in response.css('p.desc.J-desc'):
            item = DianpingItem()
            # item['titleCSSSelector'] = sel.css('a').select('@href').extract_first()
            # item['title'] = sel.xpath('./text()').extract_first()
            item['title'] = ''.join(sel.xpath('./text()').extract())
            item['link'] = ''  # sel.xpath('a/@href').extract_first()
            item['desc'] = ''  # sel.xpath('text()').extract_first()
            yield item
