import unittest
from taplist.spiders import cellarmaker
from responses import fake_response_from_file

class CellarmakerSpiderTest(unittest.TestCase):
    expected = [
            u'Admiration',
            u'Cellarmaker Porter (Batch 1)',
            u'Dank Statement',
            u'Mandarina Belgian Blonde',
            u'Quiet Echo',
            u'Simcoe Sessions',
            u'Sri Laga',
            u'Taco Hands'
    ]

    def setUp(self):
        self.spider = cellarmaker.CellarmakerSpider()

    def test_parse(self):
        response = fake_response_from_file('cellarmaker.html', self.spider.start_urls[0])
        results = self.spider.parse(response)
        names = [i['name'] for i in results]
        print repr(names)

        self.assertEqual(names, self.expected)
