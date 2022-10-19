import pandas as pd
import requests as rq
from bs4 import BeautifulSoup

page = rq.get('https://www.webtoons.com/en/genre')

soup = BeautifulSoup(page.text, 'html.parser')

# print(soup.prettify())

output_title = []
title = soup.find_all('p', class_='subj')
for i in title:
    title = i.text
    output_title.append(title)

output_author = []
author = soup.find_all('p', class_='author')
for i in author:
    author = i.text
    author = author.replace(' / ', ' ')
    output_author.append(author)
print(output_author)

output_likes = []
likes = soup.find_all('p', class_='grade_area')
for i in likes:
    like = i.find('em')
    like = like.text
    output_likes.append(like)

df = pd.DataFrame({'title': output_title, 'author': output_author, 'likes': output_likes})
df.to_csv('data/webToons.csv')