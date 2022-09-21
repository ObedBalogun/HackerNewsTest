import requests


class HackerNews:
    def __init__(self):
        self.base_url = "https://hacker-news.firebaseio.com/v0"

    def get_latest_news(self):
        resource_path = "/topstories.json?print=pretty"
        response = requests.get(f"{self.base_url}/{resource_path}")
        if response and response.status_code == 200:
            print(response.json())
            return response.json()
        else:
            print("Error")

    def get_news_details(self, news_id):
        resource_path = f"/item/{news_id}.json?print=pretty"
        response = requests.get(f"{self.base_url}/{resource_path}")
        if response and response.status_code == 200:
            print(response.json())
            return response.json()
        else:
            print("Error")
