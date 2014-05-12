import unittest
from taplist.spiders import mikkellerbar
from responses import fake_response_from_file

class MikkellerbarSpiderTest(unittest.TestCase):
    expected = [
            u'AleSmith Speedway Stout',
            u'AleSmith Wee Heavy',
            u'BFM Abbaye de Saint Bon-Chien 2012',
            u'Baird Dark Sky',
            u'Brewfist/Freigeist Galaxie Saison',
            u'Clown Shoes Chocolate Sombrero',
            u'De La Senne Band of Brothers',
            u'De Ranke Guldenberg',
            u'De Struise Brouwers Black Albert',
            u'Dieu du Ciel P\xe9nombre',
            u'Drake\u2019s Alpha Session',
            u'Faction Carlo\u2019s Imperial Stout',
            u'Firestone Walker Pivo Hoppy Pils',
            u'Fort Point Brewing Villager IPA',
            u'FreeWheel/Iron Bridge Wenlock Stout',
            u'Green Flash Road Warrior',
            u'Jolly Pumpkin Biere De Mars',
            u'Jolly Pumpkin Saison X',
            u'Lost Abbey Angel\u2019s Share Grand Cru',
            u'Magnolia In With The New IPA',
            u'Mikkeller Big Worster',
            u'Mikkeller Brettanomyces Bruxellensis',
            u'Mikkeller Fra Via Til BA',
            u'Mikkeller Milk Stout',
            u'Mikkeller Monk\u2019s Elixer',
            u'Mikkeller Orange Yuzu Glad I Said Porter (Grand Marnier)',
            u'Mikkeller Simcoe IIPA',
            u'Mikkeller Tenderloin IPA',
            u'Mikkeller Tenderloin Pale',
            u'Mikkeller Tenderloin Pilsner',
            u'Mikkeller Tenderloin Wit',
            u'Mikkeller Tiger Baby',
            u'North Coast Old No. 38 Stout (Nitro)',
            u'N\xf8gne \xd8 Winter Ale',
            u'Port Brewing Anniversary',
            u'Social Kitchen New World Lager',
            u'Tahoe Mountain Barefoot Porter (Finca Valla Galicia)',
            u'Tahoe Mountain Bright Moments',
            u'Tahoe Mountain Sugar Pine',
            u'The Bruery Hottenroth',
            u'The Bruery Sucre',
            u'Victory Prima Pils'
    ]

    def setUp(self):
        self.spider = mikkellerbar.MikkellerbarSpider()

    def test_parse(self):
        response = fake_response_from_file('mikkellerbar.html', self.spider.start_urls[0])
        results = self.spider.parse(response)
        names = [i['name'] for i in results]
        print repr(names)

        self.assertEqual(names, self.expected)
