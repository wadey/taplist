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
        beers = hxs.select("//div[preceding-sibling::div/p/span/strong = 'Draft Beers']/div[1]/p")
        items = []
        for beer in beers:
            parts = ' '.join(beer.select('text()').extract()).replace('\t', ' - ').replace('_', ' ')
            parts = re.sub(r" +", " ", parts)
            if parts and len(parts):
                i = TaplistItem()
                i['name'] = parts
                items.append(i)
        items.sort(key=lambda e: e['name'])
        return items
