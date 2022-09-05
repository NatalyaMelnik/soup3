import requests
import bs4

HEADERS = headers = {
    'authority': 'www.kith.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept-language': 'en-US,en;q=0.9',
}
KEYWORDS = ['Хостинг', 'Хранение данных', 'web', 'GitHub', 'python', 'IT', 'Программирование', 'алмаз', 'робот', 'IPhone', "Образование", "Чулан"]

base_url = 'https://habr.com'
url = base_url + '/ru/all/'
response = requests.get(url, headers=HEADERS)
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')

articles = soup.find_all('article', class_='tm-articles-list__item')
for article in articles:
    prews = [word.span.text for word in article.find_all('span', class_="tm-article-snippet__hubs-item")]
    titles = article.find("a", class_="tm-article-snippet__title-link")
    date = article.find("time").text
    href = base_url + titles['href']
    for word in prews:
        if word in KEYWORDS:
            res = f"Дата статьи {date}-->Заголовок статьи '{titles.text}'-->Ссылка на выбранную статью -->{href}"
            print(res)