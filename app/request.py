from unicodedata import name
from app import app
import urllib.request,json
from .models import news

News = news.News

# Getting API key
api_key =app.config['NEWS_API_KEY']

# Getting Base Url
base_url = app.config["BASE_URL"]

def getNews(category):

    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)

    return news_results


def get_news(name):
    get_news_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
            name = news_details_response.get('name')
            author = news_details_response.get('author')
            title = news_details_response.get('title')
            description= news_details_response.get('description')
            url = news_details_response.get('url')
            urlToImage = news_details_response.get('urlToImage')
            publishedAt = news_details_response.get('publishedAt')
            content = news_details_response.get('content')

            news_object = News(name.author,title,description,url,urlToImage,publishedAt,content)

    return news_object




def process_results(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    # name,author,title,description,urlToImage,publishedAt,content
    news_results = []
    for news_item in news_list:
        name = news_item.get('name')
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')

        if urlToImage:
            news_object = News(name,author,title,description,urlToImage,publishedAt,content)
            news_results.append(news_object)

    return news_results
