from apartment_crawler.crawler_settings import nepremicnine_filters as filters
from apartment_crawler.crawler_settings import nepremicnine_urls
from apartment_crawler.items import ApartmentItem
from pyquery import PyQuery as pq
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule

import logging

logger = logging.getLogger()


class NepremicnineSpider(CrawlSpider):
    name = 'nepremicnine'
    allowed_domains = ['nepremicnine.net']
    start_urls = nepremicnine_urls

    rules = (
        Rule(
            LinkExtractor(restrict_xpaths=('//div[@id="pagination"]/ul/li/a')),
            follow=True,
        ),
        Rule(
            LinkExtractor(restrict_xpaths=('//a[@class="slika"]')),
            callback='parse_item',
            follow=False,
        ),
    )

    def parse_item(self, response):
        try:
            i = ApartmentItem()
            self.response = response
            self.doc = pq(self.response.body)
            more_info = self.doc('#podrobnosti .more_info').text()
            i['name'] = self.doc('#content h1').text()
            i['price'] = self.doc('#podrobnosti .cena span').text()
            i['url'] = self.response.url

            if (
                self.filter_by_size(i['name']) and
                # self.filter_by_price(i['price']) and
                self.filter_by_more_info(more_info)
            ):
                return i
            # else:
            #     logger.info(
            #         'Item does not match our filters.',
            #         exc_info=True,
            #         extra=dict(
            #             stack=True,
            #             url=self.response.url,
            #             apartment_title=i['name'],
            #             raw_price=i['price'],
            #             more_info=more_info,
            #         ),
            #     )
        except Exception as e:
            logger.error(e)

    def filter_by_size(self, apartment_title: str) -> bool:
        """Parses apartment title and returns True if it matches the filter.

        `apartment_title` will be something like:

            `Prodaja, počitniški objekt, apartma: AMBROŽ POD KRVAVCEM, 58.2 m2

        """
        try:
            size = apartment_title.split(',')[-1]
            size = size.replace('m2', '').strip()
            size = float(size)
            if (filters['min_velikost'] <= size and
                    filters['max_velikost'] >= size):
                return True
            else:
                return False
        except Exception as e:
            logger.error(e, exc_info=True)
            return False

    def filter_by_price(self, raw_price: str) -> bool:
        """Parses price div and returns True if it matches the filter.

        `raw_price` will be something like:

            ` 115.000,00 €`


        NOTE: price filter atm is working via URL so this isn't necessary.
        """
        try:
            price = raw_price.replace(',00 €', '').strip()
            price = price.replace('.', '')
            price = float(price)
            if (filters['min_price'] <= price and
                    filters['max_price'] >= price):
                return True
            else:
                return False
        except Exception as e:
            logger.error(e, exc_info=True)
            return False

    def filter_by_more_info(self, more_info: str) -> bool:
        """Parses more info div and returns True if it matches the filter.

        `more_info` will be something like:

            `Posredovanje: Prodaja | Vrsta: Stanovanje | Regija: LJ-mesto | Upravna enota: Lj. Moste-Polje | Občina: Ljubljana`

        """  # noqa
        try:
            more_info = more_info.split(' | ')
            # posredovanje = more_info[0].replace('Posredovanje: ', '')
            vrsta = more_info[1].replace('Vrsta: ', '')
            regija = more_info[2].replace('Regija: ', '')
            # upravna_enota = more_info[3].replace('Upravna enota: ', '')
            obcina = more_info[4].replace('Občina: ', '')

            if(
                (vrsta in filters['regija'] or '*' in filters['vrsta']) and
                (regija in filters['regija'] or '*' in filters['regija']) and
                (obcina in filters['regija'] or '*' in filters['obcina'])
            ):
                return True
            else:
                return False

        except Exception as e:
            logger.error(e, exc_info=True)
            return False
