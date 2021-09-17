import requests
from pprint import pprint
from bs4 import BeautifulSoup

def get_response(link, keywords):
    response = requests.get(link)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, features="html.parser")
    articles = soup.findAll('article')

    # Разбираем каждую статью
    for article in articles:
        # Сохраняю все нужные блоки
        article_body = article.find('div', class_="tm-article-body tm-article-snippet__lead")
        article_title = article.find('h2', class_="tm-article-snippet__title tm-article-snippet__title_h2")
        time_section = article.find('span', class_="tm-article-snippet__datetime-published")

        # Преобразовываю текст превью во множество для поиска пересечний
        article_set = set(article_body.text.strip().split(" "))
        # Проверка на пересечение
        if keywords & article_set:
            pprint(keywords & article_set)
            # Забираем дату статьи
            for elem in time_section:
                print(elem.get('title'))
            # Забираем заголовок и ссылку на статью
            for title in article_title:
                pprint(title.text)
                pprint('https://habr.com' + title.get('href'))


if __name__ == '__main__':
    link = 'https://habr.com/ru/all'
    keywords = {'дизайн', 'фото', 'web', 'Python', 'Kubernetes' }
    get_response(link, keywords)
    pass
