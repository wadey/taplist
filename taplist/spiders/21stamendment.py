import re

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from taplist.items import TaplistItem

class t21stamendmentSpider(CrawlSpider):
    name = '21stamendment'
    allowed_domains = ['http://21st-amendment.com/']
    start_urls = ['http://21st-amendment.com/the-restaurant/']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        beers = hxs.select("//section[@id='beers-on-tap']/dl/dt")
        items = []
        for beer in beers:
            i = TaplistItem()
            parts = beer.select('text()').extract()
            parts = map(lambda s: s.strip(), parts)
            parts[0] = parts[0] + ":"
            i['name'] = ' '.join(parts)
            items.append(i)
        items.sort(key=lambda e: e['name'])
        return items
