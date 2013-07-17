from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from taplist.items import TaplistItem

class CitybeerstoreSpider(CrawlSpider):
    name = 'citybeerstore'
    allowed_domains = ['citybeerstore.com']
    start_urls = ['http://citybeerstore.com/our-menu/']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        beers = hxs.select("//div[@id='content']/p")
        items = []
        for beer in beers:
            i = TaplistItem()
            i['name'] = ' '.join(beer.select('text()').extract()).strip()
            if i['name']:
                items.append(i)
        items.sort(key=lambda e: e['name'])
        return items
