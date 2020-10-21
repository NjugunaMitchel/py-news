import  urllib.request,json
from .models import News, Article


# Getting api key
api_key = None
# Getting the movie base url
base_url = None

source_url = None

def configure_request(app):
    global api_key,base_url,source_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    source_url = app.config['SOURCE_API_URL']
      


def get_news(category):
    '''
    function that gets response from the api url
    '''
    get_news_url=base_url.format(api_key)

    with urllib.request.urlopen(get_news_url)  as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None


        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_news(news_results_list)
       
    return news_results

def process_news(sources_list):
    news_results = []
    for news_article  in sources_list:
        id = news_article.get('id')
        name = news_article.get('name')
        author = news_article.get('author')
        source=news_article.get('source')
        description = news_article.get('description')
        url = news_article.get('url')
        image = news_article.get('urlToImage')
        date = news_article.get('publishedAt')

        
        news_object = News(id,name,author,source,description,url,image,date)
        news_results.append(news_object)


    return news_results


def get_article(id):
    get_article_info_url = source_url.format(id,api_key)

    with urllib.request.urlopen(get_article_info_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_result = None
         
        if  get_article_response['article']:
           article_results_list = get_article_response['article']
           article_results = process_article(article_results_list) 

    return article_results


def process_article(articles_list):
    article_results = []
    for article_item in  articles_list:
        id = article_item.get('id')
        author = article_item('author')
        title = article_item('title')
        image = article_item('urlToImage')
        date = article_item('date')

        if image:
            article_object = Article(id,author,title,image,date)

            article_results.append(article_object)

    return article_results