import pandas as pd
import requests as rq
from bs4 import BeautifulSoup

page = rq.get('https://realpython.github.io/fake-jobs/')

soup = BeautifulSoup(page.text, 'html.parser')

print(soup.prettify())

jobTitles = soup.find_all('h2', class_='title is-5')
output_jobTitles = []
for i in jobTitles: #for x in y: 
    titles = i.text
    output_jobTitles.append(titles)

dateTime = soup.find_all('p', class_='is-small has-text-grey')
output_dateTime = []
for i in dateTime:
    date = i.text
    date = date.strip() # removes empty space on either side of text
    date = date.replace('\n', '') # removes empty lines
    date = date.replace(' ', '') # removes empty spaces
    output_dateTime.append(date)

location = soup.find_all('p', class_='location')
output_location = []
for i in location:
    location = i.text
    location = location.strip()
    output_location.append(location)

df = pd.DataFrame({'date_posted': output_dateTime,'job_title': output_jobTitles, 'location': output_location})
df.to_csv('data/job_postings.csv')