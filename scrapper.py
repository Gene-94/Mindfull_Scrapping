import requests 
from bs4 import BeautifulSoup

req = requests.get("https://www.eventbrite.com/d/online/meditation/")

soup = BeautifulSoup(req.content, "html.parser")
content = soup.find(class_='eds-event-card-content__primary-content')

link = content.find(class_='eds-event-card-content__action-link')
links = link.contents()
print(links[0])
content.find(class_='eds-event-card-content__action-link')
content.find(class_='eds-event-card-content__sub-title')