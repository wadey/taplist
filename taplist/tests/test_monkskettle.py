import unittest
from taplist.spiders import monkskettle
from responses import fake_response_from_file

class MonkskettleSpiderTest(unittest.TestCase):
    expected = [
            u'Abt 12 (8 oz) - Belgian Strong Dark - St. Bernardus, Watou, BEL - 10.5 - $10.75',
            u'Allagash White (12 oz) - Witbier - Allagash, Portland, ME - 5.2 - $5.75',
            u'Aprihop (10 oz) - IPA w/ Apricots - Dogfish Head, Milton, DE - 7.0 - $4.50',
            u'Baba (14 oz) - Black Lager - Uinta, Salt Lake City, UT - 4.0 - $5.50',
            u'Beadeca\u2019s Well (8 oz) - Smoked Porter - Thornbridge, Bakewell, ENG - 5.3 - $8.50',
            u'Blue House Citra Pale (10 oz) - Pale Ale - El Segundo, El Segundo, CA - 5.5 - $6.75',
            u'Duvel Rustica (8 oz) - Belgian Pale Ale - Ommegang, Cooperstown, NY - 8.5 - $8.75',
            u'Get Up Offa That Brown (10 oz) - Brown Ale - Golden Road, Los Angeles, CA - 5.5 - $5.50',
            u'Hopfen-Weisse (10 oz) - Weizenbock - Schneider & Sohn, Kelheim, GER - 8.3 - $7.50',
            u'Iron Throne (10 oz) - Belgian Blonde - Ommegang, Cooperstown, NY - 6.5 - $6.75',
            u'La Chouffe (12 oz) - Belgian Strong Pale - d\u2019Achouffe, Achouffe, BEL - 8.0 - $13.50',
            u'Longfin Lager (10 oz) - Munich Helles - Ballast Point, San Diego, CA - 4.2 - $6.00',
            u'Noble Rot (8 oz) - Saison - Dogfish Head, Milton, DE - 9.0 - $10.50',
            u'Obsidian \u2013 Nitro (16 oz) - Stout - Deschutes, Bend, OR - 6.4 - $6.50',
            u'Old Speckled Hen \u2013 Nitro (20 oz) - English Pale Ale - Greene King/Morland, Suffolk, ENG - 5.2 - $8.50',
            u'Reality Czeck (16 oz) - Bohemian Pilsner - Moonlight, Santa Rosa, CA - 4.8 - $6.75',
            u'Sauer Power (6 oz) - Sour Ale - Freigeist/Jester King - 5.2 - $11.75',
            u'Stone Pale Ale (16 oz) - Pale Ale - Stone, Escondido, CA - 5.4 - $6.25',
            u'The Thriller (14 oz) - Maibock - Iron Springs, Fairfax, CA - 7.5 - $6.00',
            u'Three Philosophers (8 oz) - Belgian Strong Dark - Ommegang, Cooperstown, NY - 9.8 - $10.00',
            u'Tournay Tripel (8 oz) - Tripel - Cazeau, Templeuve, BEL - 9.0 - $12.50',
            u'Twilight (16 oz) - Pale Ale - Deschutes, Bend, OR - 5.0 - $6.50',
            u'Two 5 Left (10 oz) - Imperial IPA - El Segundo, El Segundo, CA - 8.2 - $7.50',
            u'Wolf Among Weeds (10 oz) - Imperial IPA - Golden Road, Los Angeles, CA - 8.0 - $5.50'
    ]

    def setUp(self):
        self.spider = monkskettle.MonkskettleSpider()

    def test_parse(self):
        response = fake_response_from_file('monkskettle.html', self.spider.start_urls[0])
        results = self.spider.parse(response)
        names = [i['name'] for i in results]
        print repr(names)

        self.assertEqual(names, self.expected)
