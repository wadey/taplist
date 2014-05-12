from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from taplist.items import TaplistItem

import re

class CellarmakerSpider(CrawlSpider):
    name = 'cellarmaker'
    allowed_domains = ['cellarmakerbrewing.com']
    start_urls = ['http://www.cellarmakerbrewing.com']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        beers = hxs.select("//div[h4/text() = 'Currently On Tap']/div[@class='textwidget']/p/strong/text()")
        items = []
        for beer in beers:
            name = beer.extract().strip()
            if name and len(name):
                i = TaplistItem()
                i['name'] = name
                items.append(i)
        items.sort(key=lambda e: e['name'])
        return items
