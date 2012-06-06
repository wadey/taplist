import re

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from taplist.items import TaplistItem

class ZeitgeistSpider(CrawlSpider):
    name = 'zeitgeist'
    allowed_domains = ['http://www.zeitgeistsf.com/']
    start_urls = ['http://www.zeitgeistsf.com/beer.html']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        beers = hxs.select("//div[@id='main_column']/div[@id='content']/p")
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
