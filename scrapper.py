import requests 
from bs4 import BeautifulSoup
from datetime import datetime

req = requests.get("https://www.eventbrite.com/d/online/meditation/")

soup = BeautifulSoup(req.content, "html.parser")

#event_cards = soup.find_all(class_='eds-event-card-content__primary-content')
event_cards = soup.find_all("article")

for i in range(0, len(event_cards), 2):
    link = event_cards[i].find(class_='eds-event-card-content__action-link')
    title = link.h3.div.div
    image = event_cards[i].img
    event_date_string = (event_cards[i].find(class_='eds-event-card-content__sub-title')).text
    event_date_string = event_date_string.split('(')
    event_date_str = (event_date_string[0].strip())[:-4]
    date_offset = (event_date_string[1])[0:6]
    event_date = datetime.strptime(event_date_str, "%a, %b %d, %Y %I:%M %p")

    print(link.get('href'))
    print("-"*20)
    print(title.text) 
    print("-"*20)
    print(event_date_str)
    print("-"*20)
    print(date_offset)
    print("-"*20)
    print(event_date)
    print("-"*20)
    print(image.get('src'))
    print("\n"+"#"*20,"\n")

print(datetime.now())