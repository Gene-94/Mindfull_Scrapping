import requests 
from bs4 import BeautifulSoup

req = requests.get("https://www.eventbrite.com/d/online/meditation/")

soup = BeautifulSoup(req.content, "html.parser")

#event_cards = soup.find_all(class_='eds-event-card-content__primary-content')
event_cards = soup.find_all("article")

for card in event_cards:
    link = card.find(class_='eds-event-card-content__action-link')
    title = link.h3.div.div
    event_date = card.find(class_='eds-event-card-content__sub-title')
    image = card.img

    print(link.get('href'))
    print("-"*20)
    print(title.text) 
    print("-"*20)
    print(event_date.text)
    print("-"*20)
    print(image.get('src'))
    print("\n"+"#"*20,"\n")