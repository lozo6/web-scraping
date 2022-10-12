import pandas as pd
import requests as rq
from bs4 import BeautifulSoup

page = rq.get('https://pythonjobs.github.io')

soup = BeautifulSoup(page.text, 'html.parser')

output_job = []
jobListings = soup.find_all('div', class_='job')
for i in jobListings:
    job = i.find('h1').text
    output_job.append(job)

output_details = []
details = soup.find_all('p', class_='detail')
for i in details:
    det = i.text
    output_details.append(det)

df = pd.DataFrame({'date_posted': output_job,'job_title': output_details,})
df.to_csv('data/pythonJobPostings.csv')