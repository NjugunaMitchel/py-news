class News:
    '''
    News class
    '''

    def __init__(self,id,author,name,source,description,url,image,date):
        self.id = id
        self.author= author
        self.name = name
        self.source = source
        self.description = description
        self.url = url
        self.image = image
        self.date = date

class Article:
    '''
    Articles class
    '''

    def __init__(self,id,title,author,description,url,image,date):
        self.id = id
        self.title = title
        self.author= author
        self.image = image
        self.date = date