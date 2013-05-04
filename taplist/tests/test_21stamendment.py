import unittest
t = __import__('taplist.spiders.21stamendment', fromlist=['21stamendment'])
from responses import fake_response_from_file

class t21stamendmentSpiderTest(unittest.TestCase):
    expected = [
            u'5-South Pale Ale - American Pale Ale - 5.5%',
            u'Amber Waves - American Amber - 5.8%',
            u"Farmer's Daughter - Biere de Garde - 5.6%",
            u'Gigantes IPA - American IPA - 6.8%',
            u'Hell or High Watermelon Wheat - Summer on your palate - 4.9%',
            u'Heroine IPA (Guest) - American IPA - 7.2%',
            u'Imperial Jack - Imperial ESB - 8.3%',
            u'South Park Blonde - Blonde Ale - 5.1%'
    ]

    def setUp(self):
        self.spider = t.t21stamendmentSpider()

    def test_parse(self):
        response = fake_response_from_file('21stamendment.html', self.spider.start_urls[0])
        results = self.spider.parse(response)
        names = [i['name'] for i in results]
        print repr(names)

        self.assertEqual(names, self.expected)
