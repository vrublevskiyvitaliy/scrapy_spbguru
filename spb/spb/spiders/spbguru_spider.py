from scrapy import *
from ..items import SpbBuilding
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re


class SPBGuruBuildingsSpider(CrawlSpider):
    name = 'spbguru_buildings'
    allowed_domains = ["spbguru.ru"]
    start_urls = ["http://spbguru.ru/novostroyki"]

    rules = (
        Rule(LinkExtractor(allow=(r'novostroyki/\d+.no_comments', )), callback='parse_items', follow=True),
    )

    def parse_items(self, response):
        sel = Selector(response)

        all_href_cards = sel.xpath('.//*[@id=\'catalog_list\']/li/a[@class=\'n\']/@href')

        for href in all_href_cards:
            item_href = href.extract()
            yield Request(item_href, callback=self.parse_building)

    def parse_building(self, response):
        sel = Selector(response)

        item = SpbBuilding()

        item['name'] = sel.xpath('.//*[@id=\'BuildTitle\']/h1/text()').extract()
        item['spbguru_href'] = response.url
        try:
            url = sel.xpath('.//*[@class=\'topT\']//a[contains(@href, \'teaser\')]/@href').extract()[0]
            item.set_saler_href(url)
        except Exception as e:
            item['saler_href'] = ''

        item['building_card'] = self.remove_html_tags(sel.xpath('.//*[@id=\'BuildData\']').extract()[0])
        return item

    def remove_html_tags(self, html):
        TAG_RE = re.compile(r'<[^>]+>')
        return TAG_RE.sub('', html)

    parse_start_url = parse_items