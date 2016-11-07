from apartment_crawler import settings
from apartment_crawler.items import ApartmentItem
from pyquery import PyQuery as pq
from raven import Client
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from apartment_crawler.crawler_settings import nepremicnine_urls

client = Client(settings.SENTRY_DSN)


class NepremicnineSpider(CrawlSpider):
    name = 'nepremicnine'
    allowed_domains = ['nepremicnine.net']
    start_urls = nepremicnine_urls

    rules = (
        Rule(LinkExtractor(restrict_xpaths=('//div[@id="pagination"]/ul/li/a')),
             follow=True),
        Rule(LinkExtractor(restrict_xpaths=('//a[@class="slika"]')),
             callback='parse_item',
             follow=False),
    )

    def parse_item(self, response):
        try:
            i = ApartmentItem()
            self.response = response
            self.doc = pq(self.response.body)

            i['name'] = self.doc('#podrobnosti h1').text()
            i['price'] = self.doc('.cena').text()
            i['url'] = self.response.url

            return i
        except Exception as e:
            client.captureException()
            raise e
