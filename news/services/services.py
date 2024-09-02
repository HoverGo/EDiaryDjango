from ..models import News


def get_all_news():
    news = News.objects.all()
    return news


def get_one_news(id):
    news = News.objects.get(id=id)
    return news


def delete_one_news(id):
    news = News.objects.get(id=id)
    news.delete()
    return None
