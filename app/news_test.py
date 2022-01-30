import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):

    def setUp(self):

        self.new_news = News('Ars Technica','Tim De Chant','Dozens of states side with Epic in Apple App Store appeal - Ars Technica',
        'Apple’s conduct has harmed and is harming mobile app developers',
        'https://cdn.arstechnica.net/wp-content/uploads/2020/08/GettyImages-957063528-760x380.jpg',
        '2022-01-28T17:11:27Z','103 with 56 posters participating\r\nView more stories\r\nStates are siding with Epic Games as the developer appeals a lower court ruling in its antitrust lawsuit against Apple over app store fees and pa… [+2853 chars]')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

if __name__ == '__main__':
    unittest.main()