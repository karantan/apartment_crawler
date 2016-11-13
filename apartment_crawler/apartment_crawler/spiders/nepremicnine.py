from apartment_crawler.items import ApartmentItem
from pyquery import PyQuery as pq
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from apartment_crawler.crawler_settings import nepremicnine_urls

import logging

logger = logging.getLogger()


class NepremicnineSpider(CrawlSpider):
    name = 'nepremicnine'
    allowed_domains = ['nepremicnine.net']
    start_urls = nepremicnine_urls

    rules = (
        # NOTE: there is a bug on the page which ignores all filters. You need
        #       to manually add direct filter links.
        # Rule(
        #     LinkExtractor(restrict_xpaths=('//div[@id="pagination"]/ul/li/a')),
        #     follow=True,
        # ),
        Rule(
            LinkExtractor(restrict_xpaths=('//a[@class="slika"]')),
            callback='parse_item',
            follow=False,
        ),
    )

    def parse_item(self, response):
        i = ApartmentItem()
        self.response = response
        self.doc = pq(self.response.body)

        i['name'] = self.doc('#content h1').text()
        i['price'] = self.doc('#podrobnosti .cena span').text()
        i['url'] = self.response.url

        return i
