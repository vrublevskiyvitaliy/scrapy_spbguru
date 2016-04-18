# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpbBuilding(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    region = scrapy.Field()
    metro = scrapy.Field()
    address = scrapy.Field()
    date_of_ending = scrapy.Field()
    building_class = scrapy.Field()
    type_of_building = scrapy.Field()
    number_of_floors = scrapy.Field()
    amount_of_flats = scrapy.Field()
    price = scrapy.Field()
    payment_types = scrapy.Field()
    spbguru_href = scrapy.Field()
    parking = scrapy.Field()
    spbguru_company_href = scrapy.Field()
    company_name = scrapy.Field()
    permission_for_building = scrapy.Field()
    spbguru_saler_href = scrapy.Field()


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
