# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from urlparse import urlparse
import urllib2


class SpbBuilding(scrapy.Item):
    name = scrapy.Field()
    spbguru_href = scrapy.Field()
    building_card = scrapy.Field()
    saler_href = scrapy.Field()

    def set_saler_href(self, url):
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
        headers = {'User-Agent': user_agent}
        req = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(req)
        url = response.geturl()
        u = urlparse(url)
        self['saler_href'] = u.scheme + "://" + u.netloc + u.path


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
