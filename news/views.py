from newsdataapi import NewsDataApiClient

from django.contrib.auth import settings
from django.shortcuts import render

# Create your views here.

def index(request):
	api = NewsDataApiClient(apikey=settings.API_KEY)
	featured_response = api.news_api(language="en")
	sports_response = api.news_api(language="en", category="sports")
	science_response = api.news_api(language="en", category="science")
	technology_response = api.news_api(language="en", category="technology")

	featured_news = featured_response['results']
	featured_1 = featured_news[0]
	featured_2 = featured_news[1]
	featured_3 = featured_news[2]
	top_news = featured_news[3:6]

	sports_news = sports_response['results'][:6]
	science_news = science_response['results'][:6]
	technology_news = technology_response['results'][:6]
	
	context = {
		'featured_1': featured_1, 'featured_2': featured_2, 'featured_3': featured_3,
		'top_news': top_news, 'sports_news': sports_news,
		'science_news': science_news, 'technology_news': technology_news
	}
	return render(request, 'index.html', context)


def category(request, category):
	api = NewsDataApiClient(apikey=settings.API_KEY)
	response = api.news_api(language="en", category=category)
	category_news = response['results'][:9]

	context = {'category': category, 'category_news': category_news}
	return render(request, 'category.html', context)

