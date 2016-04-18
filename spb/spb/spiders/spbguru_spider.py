from scrapy import *
from ..items import SpbBuildingCard
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class SPBGuruSpider(CrawlSpider):
    name = 'spbguru'
    allowed_domains = ["spbguru.ru"]
    start_urls = ["http://spbguru.ru/novostroyki"]

    rules = (
        Rule(LinkExtractor(allow=(r'novostroyki/\d+.no_comments', )), callback='parse_items', follow=True),
    )

    def parse_items(self, response):
        sel = Selector(response)

        all_href_cards = sel.xpath('.//*[@id=\'catalog_list\']/li/a[@class=\'n\']/@href')
        items = []
        for href in all_href_cards:
            item = SpbBuildingCard()
            # item['name'] = card.xpath('a[@class=\'n\']/text()').extract()
            item['href'] = href.extract()
            # item['url'] = site.xpath('a/@href').extract()
            # item['description'] = site.xpath('text()').re('-\s[^\n]*\\r')
            items.append(item)

        return items
