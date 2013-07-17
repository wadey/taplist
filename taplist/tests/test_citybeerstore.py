import unittest
from taplist.spiders import citybeerstore
from responses import fake_response_from_file

class CitybeerstoreSpiderTest(unittest.TestCase):
    expected = [
            u'AleSmith Brewing Company, IPA',
            u'Berryessa Brewing Company, Double Tap-Double IPA',
            u'Birra Amiata, Marruca-Pale Honey Ale',
            u'Drakes Brewing Company, Blue Bottle Stout',
            u'Golden Road Brewing Company, Berlinerweisse-with lemon peel',
            u'Headlands Brewing Company, Groupe G-Belgian Rye Pale Ale',
            u'Headlands Brewing Company, Hill 88-Double IPA',
            u'Headlands Brewing Company, Point Bonita West Coast Lager',
            u'Highwater Brewing, Berliner Reisse',
            u'July 16 Tuesday Tapping:  Collection from Headlands Brewing Company',
            u'Russian River Brewing Company, Blind Pig IPA',
            u'Speakeasy, The Informant -Saison with Elder Flower',
            u'Stillwater Artisanal Ales, Existent-Dark Saison',
            u'Triple Rock, Lady Friend-Belgian Pale Ale',
            u'Van Steenberge-Monks Cafe-Flemish Red',
            u'Widmer Brewing Company, KGB-Imperial Stout'
    ]

    def setUp(self):
        self.spider = citybeerstore.CitybeerstoreSpider()

    def test_parse(self):
        response = fake_response_from_file('citybeerstore.html', self.spider.start_urls[0])
        results = self.spider.parse(response)
        names = [i['name'] for i in results]
        print repr(names)

        self.assertEqual(names, self.expected)
