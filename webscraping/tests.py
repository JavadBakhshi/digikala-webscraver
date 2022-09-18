from urllib.request import urlopen
from bs4 import BeautifulSoup
import unittest
import requests

class Test(unittest.TestCase):
   '''When you try to scrape it, it shows the posts of the site'''
   bs = None
   def setUpClass():
      url = requests.get('https://www.sporttv.pt/')
      Test.bs = BeautifulSoup(url.text, 'html.parser')
   def test_titleText(self):
      pageTitle = Test.bs.find('h1').get_text()
   def test_contentExists(self):
      content = Test.bs.find('div')
      self.assertIsNotNone(content)
if __name__ == '__main__':
   unittest.main()
