import requests


class HackerNews:
    def __init__(self):
        self.base_url = "https://hacker-news.firebaseio.com/v0"

    def get_latest_news(self):
        resource_path = "/topstories.json"
        response = requests.get(f"{self.base_url}/{resource_path}")
        if response and response.status_code == 200:
            return response.json()
        else:
            print("Error")

    def get_news_details(self, news_id):
        resource_path = f"/item/{news_id}.json"
        response = requests.get(f"{self.base_url}/{resource_path}")
        details = response.json()
        if response and response.status_code == 200:
            if details.get('deleted') or details.get('dead') or not details.get('by'):
                details['text'] = "[deleted]"
            return details
        else:
            print("Error")
