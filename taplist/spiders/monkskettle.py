from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from taplist.items import TaplistItem

import re

class MonkskettleSpider(CrawlSpider):
    name = 'monkskettle'
    allowed_domains = ['monkskettle.com']
    start_urls = ['http://monkskettle.com/index.php/menus/beer/']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        beers = hxs.select("//p[child::strong/span = 'Draft']/following-sibling::p")
        items = []
        for beer in beers:
            name = ' '.join(beer.select('text()').extract())
            if name and len(name):
                i = TaplistItem()
                i['name'] = name
                items.append(i)
        items.sort(key=lambda e: e['name'])
        return items
