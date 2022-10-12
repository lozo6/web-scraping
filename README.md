# web-scraping
HHA 507 Assignment 7

1. Create a new github repo called 'web-scraping' 

2. Using BS4, find at least 2 websites that you want to scrap data from - provide that code within a .py file  

3. In the code, for each website - create at least one dataframe that has structured data 

4. Save each of the dataframes as separate .csv files into a "/data" folder within your repo - be sure to include the .csv files within your repo (make sure they are small, < 25mb) 

4. Include a markdown file in the repo which includes instructions (e.g., what are the required python packages to run this, your approach for scrapping the data - the div/classes/css tags you found to extract the information)

## How to scrape data from a website

In this tutorial, I will be using Python version 3.9.1

First use `pip3 install pandas beautifulsoup4 requests`, these packages will be in requirements.txt

Use requests package to get website data

Use `soup = BeautifulSoup(page.text, 'html.parser')` to activate the BeautifulSoup4 package

First scan through html using `print(soup.prettify())` to see which data is able to be extracted, sometimes data is not available to be directly extracted and would need to loop through in order to extract proper data; please see .py files for more information

Using html tags and class, use `soup.findall()` to extract necessary information

Create an empty list for all data available and append data when extracting

After making necessary lists, create a DataFrame using pandas package and create new .csv file
