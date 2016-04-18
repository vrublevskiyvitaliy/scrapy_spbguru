# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpbBuilding(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    spbguru_href = scrapy.Field()
    # spbguru_company_href = scrapy.Field()

    spbguru_saler_href = scrapy.Field()
    # saler_href



class SpbCompany(scrapy.Item):
    name = scrapy.Field()
    address = scrapy.Field()
    phone = scrapy.Field()
    official_site = scrapy.Field()
    date_of_creation = scrapy.Field()
    list_of_buildings = scrapy.Field()


class SpbBuildingCard(scrapy.Item):
    name = scrapy.Field()
    href = scrapy.Field()
    # region = scrapy.Field()
    # metro = scrapy.Field()
    # company_name = scrapy.Field()
