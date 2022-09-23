from news.HackerAPI import HackerNews
from news.models import NewsItem


def fetch_news():
    # check if there are any news in the database
    # if there are, get the latest news id
    # if there are no news, get the top 100 news
    hacker_news = HackerNews()
    try:
        is_empty = NewsItem.objects.all().count() == 0
        latest_news = hacker_news.get_latest_news()
        new_item_details = []
        if is_empty:
            latest_100 = latest_news[:100]
            for news in latest_100:
                news_details = hacker_news.get_news_details(news)
                details_dict = {
                    'item_id': news_details['id'],
                    'title': news_details['title'],
                    'url': news_details['url'] if 'url' in news_details else None,
                    'text': news_details['text'] if 'text' in news_details else None,
                    'score': news_details['score'],
                    'posted_by': news_details['by'],
                    'type': news_details['type'],
                    'kids': news_details['kids'] if 'kids' in news_details else None,
                }
                news_item = NewsItem(**details_dict)
                new_item_details.append(news_item)
                print("done")
        else:
            latest_news_id = NewsItem.objects.all().latest('created').item_id
            index_of_latest_news = latest_news.index(latest_news_id)
            for news_id in latest_news[(index_of_latest_news + 1):(100 + index_of_latest_news)]:
                news_details = hacker_news.get_news_details(news_id)
                details_dict = {
                    'item_id': news_details['id'],
                    'title': news_details['title'],
                    'url': news_details['url'] if 'url' in news_details else None,
                    'text': news_details['text'] if 'text' in news_details else None,
                    'posted_by': news_details['by'],
                    'score': news_details['score'],
                    'type': news_details['type'],
                    'kids': news_details['kids'] if 'kids' in news_details else None,
                }
                news_item = NewsItem(**details_dict)
                new_item_details.append(news_item)
        NewsItem.objects.bulk_create(new_item_details)
    except Exception as e:
        print(e)


