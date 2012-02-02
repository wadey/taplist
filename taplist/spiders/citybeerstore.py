from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from taplist.items import TaplistItem

class CitybeerstoreSpider(CrawlSpider):
    name = 'citybeerstore'
    allowed_domains = ['www.citybeerstore.com']
    start_urls = ['http://www.citybeerstore.com/beer-store/menu']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        beers = hxs.select("//ul[@class='beerlist']/li")
        items = []
        for beer in beers:
            i = TaplistItem()
            i['name'] = beer.select('text()').extract()
            items.append(i)
        return items
