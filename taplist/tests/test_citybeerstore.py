import unittest
from taplist.spiders import citybeerstore
from responses import fake_response_from_file

class CitybeerstoreSpiderTest(unittest.TestCase):
    expected = [
            u'AleSmith "Horny Devil"',
            u'Bavik "Monk\'s Cafe" Sour Red',
            u'Brasserie Dubuisson "Cuvee des Trolls"',
            u'Brasserie Dupont "Monk\'s Stout"',
            u'Brouwerij Verhaeghe "Duchesse De Bourgogne" Flemish Sour Ale',
            u'Deschutes "Chainbreaker"',
            u'Golden Road "Berliner Weiss"',
            u'Golden Road "It\'s Not Always Sunny in LA"',
            u'Golden Road "Point the Way" IPA',
            u'Golden Road "Wolf Among Weeds" DIPA',
            u'Lagunitas "Waldos\' 420 Mystery Beer"',
            u'Marin and CBS "Platypus, Batch 2" Imperial Stout',
            u'Petus "Sour Pale Ale"',
            u'Russian River "Row 2 Hill 56"',
            u'Stillwater "Folklore" Stout'
    ]

    def setUp(self):
        self.spider = citybeerstore.CitybeerstoreSpider()

    def test_parse(self):
        response = fake_response_from_file('citybeerstore.html', self.spider.start_urls[0])
        results = self.spider.parse(response)
        names = [i['name'] for i in results]
        print repr(names)

        self.assertEqual(names, self.expected)
