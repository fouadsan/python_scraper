from bs4 import BeautifulSoup

with open('src/test_example.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# result = soup.find('h1', id='big_title')
articles = soup.find_all('div', class_='article')

# print(article)

for article in articles:
    title = article.h2.a.text
    print(title)

    description = article.p.text
    print(description)

    print()
