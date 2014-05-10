import unittest
from taplist.spiders import citybeerstore
from responses import fake_response_from_file

class CitybeerstoreSpiderTest(unittest.TestCase):
    expected = [
            u'Alpine Beer Company - Nelson IPA-Golden Rye IPA',
            u'Brouwerij Lupus - Wolf 7-Golden Belgian Ale',
            u'Drakes Brewing Company - Unite Pale Ale',
            u'Epic Brewing Company - Pumpkin Porter',
            u"Evil Twin Brewing  - Apple Brandy Sour Lil' B-Sour-Sour Stout",
            u'Golden Road Brewing  - 329 Lager',
            u'Hangar 24 Craft Brewery - Betty IPA-American Style IPA',
            u'Hangar 24 Craft Brewery - California Spring Beer-Hoppy Belgian blend',
            u'Hangar 24 Craft Brewery - Chocolate Porter',
            u'High Water Brewing  - No Boundary IPA',
            u'Off Color Brewing - Troublesome Gose',
            u'Russian River Brewing Company - Aud Blonde Ale',
            u'Stone Brewing Company - 2011 Stone Imperial Russian Stout-IRS',
            u'The Bruery - Hottenroth-Berliner Weisse',
            u'The Lost Abbey - Agave Maria-Tequila barrel aged ale'
    ]

    def setUp(self):
        self.spider = citybeerstore.CitybeerstoreSpider()

    def test_parse(self):
        response = fake_response_from_file('citybeerstore.html', self.spider.start_urls[0])
        results = self.spider.parse(response)
        names = [i['name'] for i in results]
        print repr(names)

        self.assertEqual(names, self.expected)
