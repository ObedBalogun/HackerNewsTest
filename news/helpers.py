from news.HackerAPI import HackerNews
from news.models import NewsItem, Comment


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

                    'type': news_details['type'],
                    'kids': news_details['kids'] if 'kids' in news_details else None,
                }
                news_item = NewsItem(**details_dict)
                new_item_details.append(news_item)
        else:
            for news_id in latest_news:
                news_details = hacker_news.get_news_details(news_id)
                details_dict = {
                    'item_id': news_details['id'],
                    'title': news_details['title'],
                    'url': news_details['url'] if 'url' in news_details else None,
                    'text': news_details['text'] if 'text' in news_details else None,
                    'score': news_details['score'],
                    'type': news_details['type'],
                    'kids': news_details['kids'] if 'kids' in news_details else None,
                }
                news_item = NewsItem(**details_dict)
                new_item_details.append(news_item)
        NewsItem.objects.bulk_create(new_item_details)
    except Exception as e:
        print(e)


def resolve_comments():
    # get all the news items
    # for each news item, get the comments
    # for each comment, get the comment details
    # create a comment object
    # save the comment object
    all_news_items = NewsItem.objects.filter(kids__isnull=False).values_list('item_id', 'kids')
    hacker_news = HackerNews()
    comment_list = []
    for item in all_news_items:
        comment_list = item[1]
        if len(comment_list) > 0:
            for comment in comment_list:
                get_comment_details = hacker_news.get_news_details(comment)
                parent_article = NewsItem.objects.get(item_id=item[0])
                comment_details = {"commenter": get_comment_details['by'],
                                   "comment_id": get_comment_details['id'],
                                   "parent_id": get_comment_details['parent'],
                                   "parent_article": parent_article,
                                   "text": get_comment_details['text'],
                                   "type": get_comment_details['type'],
                                   "deep_comments": get_comment_details[
                                       'kids'] if 'kids' in get_comment_details else None,
                                   "timestamp": get_comment_details['time']
                                   }
                comment_object = Comment(**comment_details)
                comment_list.append(comment_object)
    Comment.objects.bulk_create(comment_list)
