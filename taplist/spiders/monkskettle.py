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
        i = TaplistItem()
        bee
        #i['domain_id'] = hxs.select('//input[@id="sid"]/@value').extract()
        #i['name'] = hxs.select('//div[@id="name"]').extract()
        #i['description'] = hxs.select('//div[@id="description"]').extract()
        return i
