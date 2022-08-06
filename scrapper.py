import requests 
from bs4 import BeautifulSoup

req = requests.get("https://www.eventbrite.com/d/online/meditation/")

soup = BeautifulSoup(req.content, "html.parser")
event_card = soup.find(class_='eds-event-card-content__primary-content')

link = event_card.find(class_='eds-event-card-content__action-link')
title = link.h3
event_date = event_card.find(class_='eds-event-card-content__sub-title')


print(link)
print("-"*20)
print(title)
print("-"*20)
print(event_date)