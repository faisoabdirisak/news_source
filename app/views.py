from flask import render_template
from app import app
from app.models import news
from .request import getNews,get_news

# Views
@app.route('/')
def index():
    content_news = getNews('content')
    tech_news = getNews('tech')
    articles_news = getNews('articles')
    title = 'Home - Faska News Channel'
    return render_template('index.html', title = title,content= content_news,tech=tech_news,articles=articles_news)
   
@app.route('/news/<name>')
def news(name):

    '''
    View movie page function that returns the movie details page and its data
    '''
    news = getNews(name)
    title = f'{name}'

    return render_template('news.html',title=title,news= news)    