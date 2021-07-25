import string

import requests
from bs4 import BeautifulSoup
import os

BASE_URL = "https://www.nature.com"

print("This will scrape articles in the Nature website")
pages = int(input("Number of article pages to scrape: "))
article_type = input("Article type to scrape:")


def get_data(url):
    print("getting data %", url)
    r = requests.get(url)
    return BeautifulSoup(r.content, 'html.parser')


for i in range(pages):
    i = i + 1
    articles_page = f"/nature/articles?searchType=journalSearch&sort=PubDate&page={i}"
    folder_name = f"Page_{i}"
    if not os.access(folder_name, os.F_OK):
        os.mkdir(folder_name)
    file_dir = os.path.join(os.getcwd(), f"Page_{i}")

    articles_saved = []
    articles = get_data(BASE_URL + articles_page).findAll('li', class_={'app-article-list-row__item'})

    for article in articles:
        # Check if article has correct type
        if article.find('span', class_="c-meta__type").text == article_type:
            item = article.find('a', {'data-track-action': 'view article'})
            article_link = item.get('href')
            parser = get_data(BASE_URL + article_link)

            # Getting article title
            title = parser.find('h1').text
            title = title.translate(str.maketrans('', '', string.punctuation))
            title = title.strip().replace(" ", "_")

            # Getting article body text
            body = parser.find('div', class_='c-article-body u-clearfix')
            if body is None:
                body = parser.find('div', class_='article-item__body')
            text = body.text.strip()

            file_name = os.path.join(file_dir, f"{title}.txt")
            f = open(file_name, "wb")
            f.write(text.encode())
            f.close()
            articles_saved.append(file_name)
    print(f"Saved articles:  {articles_saved}")

print("All articles were scraped.")
