from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news,get_article
from ..models import News,Article



@main.route('/')
def index():
    '''
    landing
    '''
    top_headlines = get_news('top_headlines')
    sports_news = get_news('sports')
    business_news = get_news('business')

    title = 'Trending'
    
    print(top_headlines)
    return render_template('index.html',title = title,top_headlines = top_headlines, sports = sports_news,business = business_news)

""" @main.route('/news/<id>')
def article(id):
     article = get_news(id)

     general = get_news('general')
     bussiness = get_news('bussiness')
     return render_template('news.html',general=  general,bussiness = bussiness) """



@main.route('/search/<source>')
def search(source):
    news_source_list = source.split(' ')
    news_source_format = '+'.join(news_source_list)
    searched_sources = search_news(news_source_format)

    title = f'Results for {source}'

    return render_template('news.html',news = searched_sources)