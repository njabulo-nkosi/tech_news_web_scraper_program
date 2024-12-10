import requests
from bs4 import BeautifulSoup


class TechNews:

    def __init__(self):
        pass

    def get_dev_news(self):
        devto_url = 'https://dev.to/top/week'

        response = requests.get(url=devto_url)
        website_html = response.text

        soup = BeautifulSoup(website_html, 'html.parser')

        dev_articles = soup.find_all(name='h2', class_='crayons-story__title')

        top_10_articles = [article.getText().strip() for article in dev_articles[:10]]

        # print(f'For further reading, please access the following endpoint: {devto_url}')
        return top_10_articles

    def get_ai_news(self):
        tech_crunch_url = 'https://techcrunch.com/category/artificial-intelligence/'

        response = requests.get(url=tech_crunch_url)
        website_html = response.text

        soup = BeautifulSoup(website_html, 'html.parser')

        ai_articles = soup.find_all(name='h3', class_='loop-card__title')

        top_10_articles = [article.getText().strip() for article in ai_articles[:10]]

        # print(f'For further reading, please access the following endpoint: {tech_crunch_url}')
        return top_10_articles
