from apartment_crawler import settings
from apartment_crawler.items import ApartmentItem
from pyquery import PyQuery as pq
from raven import Client
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from apartment_crawler.crawler_settings import bolha_urls

client = Client(settings.SENTRY_DSN)


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
        try:
            i = ApartmentItem()
            self.response = response
            self.doc = pq(self.response.body)

            i['name'] = self.doc(".ad h1").text()
            i['price'] = self.doc(".price span").text()
            i['url'] = self.response.url

            return i
        except Exception as e:
            client.captureException()
            raise e
