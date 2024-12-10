import smtplib
from news_scraper import TechNews
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

MY_EMAIL = os.getenv('MY_EMAIL')
PASSWORD = os.getenv('PASSWORD')

tech_news = TechNews()

devto_top_articles = tech_news.get_dev_news()

print(devto_top_articles)

top_ai_articles = tech_news.get_ai_news()

print(top_ai_articles)

try:
    with open(file='last_date_sent.txt', mode='r') as date_file:
        last_date_sent = datetime.fromisoformat(date_file.read().strip())
except FileNotFoundError:
    last_date_sent = datetime.now() - timedelta(days=2)

current_date = datetime.now()

# if True:
if current_date >= last_date_sent + timedelta(days=1):

    devto_formatted = '\n'.join([f'{i + 1}. {article}' for i, article in enumerate(devto_top_articles)])
    top_ai_formatted = '\n'.join([f'{i + 1}. {article}' for i, article in enumerate(top_ai_articles)])

    message = (f'Subject: Latest Tech, Software & AI News\n\n'
               f'Dev-to Top Articles:\n'
               f'{devto_formatted}\n\n'
               f'TechCrunch Top AI Articles:\n'
               f'{top_ai_formatted}'
               )

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs='njabu.nkosi1@gmail.com',
                            msg=message.encode('utf-8')
                            )
        print(f'For further reading, please access the following endpoint(s): https://dev.to/top/week and '
              f'https://techcrunch.com/category/artificial-intelligence/; respectively.')
