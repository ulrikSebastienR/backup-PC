#http://samranga.blogspot.com/2015/08/web-scraping-beginner-python.html
from bs4 import BeautifulSoup
import urllib3
url = 'http://www.imdb.com/search/title?release_date=2010,2020&title_type=feature&user_rating=1.0,10'