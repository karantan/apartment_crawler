# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field
from scrapy import Item


class ApartmentItem(Item):
    name = Field()
    price = Field()
    url = Field()
    referencna_st = Field()
    created = Field()
