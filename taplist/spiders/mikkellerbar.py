from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from taplist.items import TaplistItem

import re

class MikkellerbarSpider(CrawlSpider):
    name = 'mikkellerbar'
    allowed_domains = ['mikkellerbar.com']
    start_urls = ['http://www.mikkellerbar.com/ontap.html']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        beers = hxs.select("//div[@id='on_tap_menu']/p")
        items = []
        for beer in beers:
            name = ' '.join(beer.select('descendant-or-self::*/text()').extract()).strip()
            if name and len(name) and '|' in name:
                name = name.replace(u'\xa0', u' ')
                name = re.sub(r'\s+', ' ', name)
                name = re.sub(r'\s+\|.*$', '', name)
                i = TaplistItem()
                i['name'] = name
                items.append(i)
        items.sort(key=lambda e: e['name'])
        return items
