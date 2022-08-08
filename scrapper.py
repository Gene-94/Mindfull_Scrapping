import requests 
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil.relativedelta import relativedelta




req = requests.get("https://www.eventbrite.com/d/online/meditation/")

soup = BeautifulSoup(req.content, "html.parser")

while True:
    try:
        timezone = input("Insert your timezone in UTC (ex: UTC+1 or UTC-3) : UTC")
        int(timezone)
        break
    except:
        print("Incorrect format, don't forget the 'UTC' is already there just insert the diference (ex: '-1' or '+2')")

#event_cards = soup.find_all(class_='eds-event-card-content__primary-content')
event_cards = soup.find_all("article")

print("### Mindfullness & Meditation ###")
print("Check all the upcoming events in the next 48 hours")

for i in range(0, len(event_cards), 2):
    link = event_cards[i].find(class_='eds-event-card-content__action-link')
    title = link.h3.div.div
    image = event_cards[i].img
    event_date_string = (event_cards[i].find(class_='eds-event-card-content__sub-title')).text
    event_date_string = event_date_string.split('(')
    event_date_str = (event_date_string[0].strip())[:-4]
    date_offset = (event_date_string[1])[0:6]
    event_date = datetime.strptime(event_date_str, "%a, %b %d, %Y %I:%M %p")

    try:    
        date_offset = int(date_offset[0:3])
    except:
        date_offset = 0
        print("An error, regarding the date and time, has ocurred. Unable to parse the timezone correctly.")
      
    date_offset = eval(str(date_offset)+timezone)
    event_date = event_date - relativedelta(hours=date_offset)

    if((event_date + relativedelta(hours=48)) >= datetime.now()):
        
        print("-"*20)
        print(title.text) 
        print(event_date,"UTC"+timezone)
        print("see more about -> "+link.get('href'))
        #print(image.get('src'))
        print("-"*20)



#To Do: Email the filtered list to a given email 

