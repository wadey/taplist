import unittest
from taplist.spiders import zeitgeist
from responses import fake_response_from_file

class ZeitgeistSpiderTest(unittest.TestCase):
    expected = [
            u'"Black Butte Porter" - Deschutes Brewing Co.: Bend, OR',
            u'"Damnation" Belgian-Style Strong Golden Ale: Russian River Brewing Co. Santa Rosa, CA',
            u'"Death & Taxes" Black Lager: Moonlight Brewing Co. Santa Rosa, CA',
            u'"Downtown Brown" - Lost Coast Brewing Co.: Eureka,CA',
            u'"Great White" California Wheat - Lost Coast Brewing Co.: Eureka, CA',
            u'"Hoegaarden Wit" White Wheat - Belgium:',
            u'"Lagunitas" IPA - Lagunitas Brewing Co.: Petaluma, CA',
            u'"Mirror Pond" Pale Ale - Deschutes Brewing: Bend, OR',
            u'"Poppy Jasper" Amber Ale - El Toro Brewing Co.: Morgan Hill, CA',
            u'"Racer 5" IPA - Bear Republic Brewing Co.: Healdsburg, CA',
            u'"Stella Artois" Lager - Belgium:',
            u'"Total Domination" IPA - Ninkasi Brewing Co.: Eugene, OR',
            u'"Trumer Pils" - Berkeley/Austria:',
            u'Anchor "Steam" Beer (Lager): Anchor Brewing Co. San Francisco, CA',
            u'Franziskaner Hefeweizen - Germany:',
            u'Sierra Nevada "Pale Ale" - Sierra Nevada Brewing Co.: Chico, CA'
    ]

    def setUp(self):
        self.spider = zeitgeist.ZeitgeistSpider()

    def test_parse(self):
        response = fake_response_from_file('zeitgeist.html', self.spider.start_urls[0])
        results = self.spider.parse(response)
        names = [i['name'] for i in results]
        print repr(names)

        self.assertEqual(names, self.expected)
