from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule

import logging

logger = logging.getLogger()


class SalomonSpider(CrawlSpider):
    name = 'salomon'
    allowed_domains = ['salomon.si']
    start_urls = ['http://salomon.si/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        return i
