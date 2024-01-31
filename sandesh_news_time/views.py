# ------------------------------IMPORTING MODULES--------------------------------------

from django.shortcuts import render
import requests
import json
from django.http import HttpResponse
from django.contrib import messages

# ---------------------------------CREATING VIEWS---------------------------------------------------
def home(request):
    return render(request, 'sandesh_news_time/index.html')

def news(request):
    news_title = ""
    news_desc = ""
    news_img = ""
    news_url = ""
    if request.method == 'GET':
        newslist = []
        category = request.GET.get('category', "")
        if len(category)>0:
            r = requests.get(f'https://newsapi.org/v2/everything?q={category}&from=2023-12-26&sortBy=publishedAt&language=en&apiKey=c92cbf9982c0481eb88731c590acafad')
            c_status = r.status_code
            print(c_status)
            khabar = json.loads(r.text)
            if "articles" in khabar:
                for m_news in khabar["articles"]:
                    news_title = m_news.get("title", "Not found")
                    news_desc = m_news.get("description", "Not found")
                    news_img = m_news.get("urlToImage", "Image not Found")
                    news_url = m_news.get("url", " ")
                    newslist.append({"title":news_title, "n_desc":news_desc, "n_image":news_img, "n_url":news_url})

            

        else:
            messages.info(request, "Please enter a keyword to fetch related news")

        
    
    return render(request, 'sandesh_news_time/news.html',{"title":news_title,"n_desc":news_desc,"newslist":newslist, "n_image":news_img, 'cat':category, 'n_url':news_url})