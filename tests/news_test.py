import unittest
from app.models import news

class NewsTest(unittest.TestCase):
    '''
    test class for the news class
    '''
    def setup(self):
        '''
        runs before any test
        '''

        self.new_news = News(334,'BBC','Microsoft','trail data','http://newsapi.org/v2/{}?apikey={}','enen',23)

        def tst_instance(self):
            self.assertTrue(isinstance(self.new_news))

if __name__ == '__main__':
    unittest.main()
