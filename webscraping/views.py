from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from rest_framework import generics
from .serializers import ScrapeSerializer
from .models import Scrape


url = "https://www.digikala.com/search/category-mobile-phone/product-list/?price%5Bmax%5D=727221278&price%5Bmin%5D=0&sort=21"
titles = []
stars = []
prices = []
for page in range(1, 3):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    results = soup.find_all('div', attrs={'class':'px-5'})
    titles = ['']
    for result in results:
        title = result.find('div', attrs={'class': 'nth-child'}).find('div', attrs={'class': 'd-flex.grow-1.pos-relative.flex-row'}) # result not results
        price = result.find('div', attrs={'class': 'nth-child'}).text[13:-11]
        titles.append((title, price,))

new_rss = Scrape(
    title = titles,
    url = 'https://www.digikala.com/search/category-mobile-phone/product-list/?price%5Bmax%5D=727221278&price%5Bmin%5D=0&sort=21'
)

new_rss.save()


 
class Home(generics.ListAPIView):
    serializer_class = ScrapeSerializer
    queryset = Scrape.objects.all()
    
    


