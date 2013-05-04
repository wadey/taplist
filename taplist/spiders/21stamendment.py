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
        beers = hxs.select("//section[@id='beers-on-tap']/dl")
        names = beers.select("//dt")
        types = beers.select("//dd[@class='ontap-type']")
        abvs = beers.select("//dd[@class='ontap-abv']")
        full = zip(names, types, abvs)
        items = []
        for beer in full:
            i = TaplistItem()
            i['name'] = ' - '.join([' '.join(part.select('text()').extract()) for part in beer])
            items.append(i)
        items.sort(key=lambda e: e['name'])
        return items
