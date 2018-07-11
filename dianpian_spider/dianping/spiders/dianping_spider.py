# coding=utf-8

import scrapy
import sys
import logging
from tutorial.items import DmozItem

reload(sys)
sys.setdefaultencoding('utf-8')


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["www.ruanyifeng.com"]
    start_urls = [
        "http://www.ruanyifeng.com/blog/2014/02/",
    ]

    def parse(self, response):

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

            item = DmozItem()
            item['titleCSSSelector'] = sel.css('a').select('@href').extract_first()
            item['title'] = sel.xpath('a/text()').extract_first()
            item['link'] = sel.xpath('a/@href').extract_first()
            item['desc'] = sel.xpath('text()').extract_first()
            yield item
