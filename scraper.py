from bs4 import BeautifulSoup
import requests
import csv

# Scraping my personal website 😂 (Services section) and export infos to csv file.

source = requests.get('https://fouadben.herokuapp.com').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('scraped.csv', 'w')

csv_writer = csv.writer(csv_file)

csv_writer.writerow(['title', 'description', 'icon_link'])

services = soup.find_all('div', class_='service-item')
for service in services:
    title = service.h4.text
    print(title)
    description = service.p.text
    print(description)

    try:  # to avoid code break in case there is no icon in the service item, you can apply it above also.
        icon_src = service.img['src']
        print(icon_src)
    except Exception as e:
        icon_src = None

    print()

    csv_writer.writerow([title, description, icon_src])

csv_file.close()
