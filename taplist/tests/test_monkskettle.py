import unittest
from taplist.spiders import monkskettle
from responses import fake_response_from_file

class MonkskettleSpiderTest(unittest.TestCase):
    expected = [
            u'1903 (10 oz) Pale Lager Craftsman, Pasadena, CA 5.6 $6.00',
            u'ABT 12 (8 oz) Belgian Strong Dark St. Bernardus, Watou, BEL 10.5 $10.75',
            u'Allagash White (12 oz) Witbier Allagash, Portland, ME 5.2 $6.00',
            u'Ashtray Heart (8 oz) Smoked Stout Evil Twin, Brooklyn, NY 8.9 $8.50',
            u'Back In Black (16 oz) Black IPA 21st Amendment, San Francisco, CA 6.8 $6.50',
            u'Blue House Citra Pale (10 oz) Pale Ale El Segundo, El Segundo, CA 5.5 $6.75',
            u'Bluebird XB (10 oz) Pale Ale Coniston, Coniston, ENG 4.4 $7.00',
            u'Chestnut Porter (10 oz) Porter w/ Chestnut Jolly Pumpkin, Dexter, MI 5.7 $8.75',
            u'Death & Taxes (16 oz) Black Lager Moonlight, Santa Rosa, CA 5.0 $7.00',
            u'Dixon California Nugget (16 oz) Amber Ale Ruhstaller, Sacramento, CA 5.6 $7.50',
            u'Ellie\u2019s Brown (16 oz) Brown Ale Avery, Boulder, CO 5.5 $6.75',
            u'Fire and Blood-Game of Thrones(10 oz)Amber Ale Ommegang, Cooperstown, NY 6.8 $6.75',
            u'Gouden Carolus Easter Ale (8 oz) Belgian Strong Dark Het Anker, Mechelen, BEL 10.5 $12.75',
            u'Hen House Saison (10 oz) Saison Hen House, Petaluma, CA 5.5 $5.00',
            u'Li\u2019l Devil (10 oz) Belgian Pale Alesmith, San Diego, CA 5.75 $5.00',
            u'Malheur 10\xb0 (8 oz) Belgian Strong Pale Malheur, Buggenhout, BEL 10.0 $11.50',
            u'Meltdown (10 oz) Imperial IPA Midnight Sun, Anchorage, AK 8.0 $8.75',
            u'No Boundry (10 oz) IPA High Water, San Leandro, CA 6.5 $5.75',
            u'Pinedrops (16 oz) IPA Deschutes, Bend, OR 6.5 $7.00',
            u'Pliny the Elder (16 oz) Imperial IPA Russian River, Santa Rosa, CA 8.0 $8.50',
            u'Reality Czeck (16 oz) Bohemian Pilsner Moonlight, Santa Rosa, CA 4.8 $7.00',
            u'Russian Imperial Stout (10 oz) Russian Imperial Stout Golden Road, Los Angeles, CA 8.7 $5.50',
            u'Stone Pale (16 oz) Pale Ale Stone, Escondido, CA 5.4 $7.00',
            u'Valley of the Heart\u2019s Delight (8 oz) Wild Ale w/ Fruit Almanac, San Francisco, CA 7.0 $6.50'
    ]

    def setUp(self):
        self.spider = monkskettle.MonkskettleSpider()

    def test_parse(self):
        response = fake_response_from_file('monkskettle.html', self.spider.start_urls[0])
        results = self.spider.parse(response)
        names = [i['name'] for i in results]
        print repr(names)

        self.assertEqual(names, self.expected)
