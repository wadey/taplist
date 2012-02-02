from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from taplist.items import TaplistItem

class MonkskettleSpider(CrawlSpider):
    name = 'monkskettle'
    allowed_domains = ['monkskettle.com']
    start_urls = ['http://monkskettle.com/index.php/menus/beer/']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        beers = hxs.select("//div[preceding-sibling::div[2]/p/span = 'Draught Beers']/p[@class='USE-FOR-ALL-BEER']")
        #beers = hxs.select("//p[@class='USE-FOR-ALL-BEER']/span[@class='char-style-override-3']")
        items = []
        for beer in beers:
            i = TaplistItem()
            parts = ' '.join(beer.select('span/text()').extract()).replace('\t', ' - ')
            if parts and len(parts):
                i['name'] = parts
                items.append(i)
        items.sort(key=lambda e: e['name'])
        return items
