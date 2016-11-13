from apartment_crawler.items import ApartmentItem
from pyquery import PyQuery as pq
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from apartment_crawler.crawler_settings import bolha_urls

import logging

logger = logging.getLogger()


class BolhaSpider(CrawlSpider):
    name = 'bolha'
    allowed_domains = ['bolha.com']
    start_urls = bolha_urls

    rules = (
        Rule(
            LinkExtractor(restrict_xpaths=(
                '//div[@id="toolBox-top"]//a[@class="forward"]')),
            follow=True,
        ),
        Rule(
            LinkExtractor(restrict_xpaths=(
                '//div[@class="coloumn image"]')),
            callback='parse_item',
            follow=False,
        ),
    )

    def parse_item(self, response):
        i = ApartmentItem()
        self.response = response
        self.doc = pq(self.response.body)

        i['name'] = self.doc(".ad h1").text()
        i['price'] = self.doc(".price span").text()
        i['url'] = self.response.url

        return i
