import unittest
t = __import__('taplist.spiders.21stamendment', fromlist=['21stamendment'])
from responses import fake_response_from_file

class t21stamendmentSpiderTest(unittest.TestCase):
    expected = [
            u'5-South Pale Ale',
            u'Amber Waves', u"Farmer's Daughter",
            u'Gigantes IPA',
            u'Hell or High Watermelon Wheat',
            u'Heroine IPA (Guest)',
            u'Imperial Jack',
            u'South Park Blonde'
    ]

    def setUp(self):
        self.spider = t.t21stamendmentSpider()

    def test_parse(self):
        response = fake_response_from_file('21stamendment.html', self.spider.start_urls[0])
        results = self.spider.parse(response)
        names = [i['name'] for i in results]
        print repr(names)

        self.assertEqual(names, self.expected)
