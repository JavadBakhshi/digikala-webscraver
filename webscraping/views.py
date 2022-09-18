from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
from .models import Scrape
from .serializers import ScrapeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics


html = requests.get('https://www.digikala.com/search/category-mobile-phone/')
soup = BeautifulSoup(html.text, 'html.parser')
name = soup.select('#\32 5 > div > div:nth-child(1) > a > article > div.d-flex.grow-1.pos-relative.flex-row > div.grow-1.d-flex.flex-column.ai-stretch.jc-start')


titles = []


for header in name:
    titles.append(header.text)
    # titles = titles.strip()
    


new_rss = Scrape(
    title = titles, 
    url = 'https://www.digikala.com/search/category-mobile-phone/product-list/?price%5Bmax%5D=727221278&price%5Bmin%5D=0&sort=21'
)

new_rss.save()


 
class Home(generics.ListAPIView):
    serializer_class = ScrapeSerializer
    queryset = Scrape.objects.all()
    
    


