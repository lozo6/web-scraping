import pandas as pd
import requests as rq
from bs4 import BeautifulSoup

page = rq.get('https://pcpartpicker.com/guide/')

soup = BeautifulSoup(page.text, 'html.parser')

# print(soup.prettify())

output_title = []
title = soup.find_all('h1', class_='guide__title')
for i in title:
    title = i.text
    output_title.append(title)
# print(output_title)

output_cpu = []
output_gpu = []
description = soup.find_all('ul', class_='guide__keyProducts list-unstyled')
for i in description:
    parts = i.text
    parts = parts.strip().split('\n')
    cpu = parts[0]
    gpu_case = parts[1]
    output_cpu.append(cpu)
    output_gpu.append(gpu_case)
# print(output_cpu)
# print(output_gpu)

df = pd.DataFrame({'title': output_title,'cpu': output_cpu, 'gpu/case': output_gpu})
df.to_csv('data/pcPartPicker.csv')