from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from taplist.items import TaplistItem

class CitybeerstoreSpider(CrawlSpider):
    name = 'citybeerstore'
    allowed_domains = ['citybeerstore.com']
    start_urls = ['http://citybeerstore.com/menu/']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        taps = hxs.select("//div[contains(concat(' ', @class, ' '), ' taps ')]")
        beers = taps.select("ul/li[contains(concat(' ', @class, ' '), ' beer ')]")
        items = []
        for beer in beers:
            i = TaplistItem()
            brewery = beer.select("div[@class='brewery']/text()").extract()
            name = beer.select("div[@class='name']/text()").extract()
            i['name'] = ' '.join(brewery + ['-'] + name).strip()
            if i['name']:
                items.append(i)
        items.sort(key=lambda e: e['name'])
        return items
