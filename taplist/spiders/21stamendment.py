import re

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from taplist.items import TaplistItem

class t21stamendmentSpider(CrawlSpider):
    name = '21stamendment'
    allowed_domains = ['http://21st-amendment.com/']
    start_urls = ['http://21st-amendment.com/restaurant/ontap']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        beers = hxs.select("//div[contains(@class,'fullBeerSlot')]")
        items = []
        for beer in beers:
            i = TaplistItem()
            name = ' '.join(beer.select('img/@alt').extract())
            if not name:
                name = ' '.join(beer.select("div[contains(@class,'imgSlug')]/text()").extract())
            desc = ' '.join(beer.select('span/text()').extract())

            i['name'] = re.sub(r' +', ' ', ' '.join([name, desc]))
            items.append(i)
        items.sort(key=lambda e: e['name'])
        return items
