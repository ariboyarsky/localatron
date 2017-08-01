# This file will scrape training, tuning, and test data from various news sources

import requests
from bs4 import BeautifulSoup as bs

# local data
# we will collect 100 articles from each site
local_urls = ['http://www.nbcwashington.com/news/local/', 'http://wtop.com/region/local/', 'http://www.nbcnewyork.com/news/local/',
        "http://www.latimes.com/local/", "http://www.nbcchicago.com/news/local/", "http://6abc.com/philadelphia/",
        "http://5newsonline.com/",  "http://wnct.com/", "http://www.mynbc5.com/local-news",
        "http://www.heraldcourier.com/news/", "http://www.abc57.com/"]

# collect first 100 links to an article store in dict based on above url
# output each article to a txt file under training, local-00i.txt

# national data
# collect 220 from each
natl_urls = ["https://www.usnews.com/news/national-news", "http://www.foxnews.com/", "http://www.nbcnews.com/news/us-news",
             "http://www.latimes.com/nation/", "http://www.cnn.com/"]

# collect first 100 links to an article store in dict based on above url
# output each article to a txt file under training, national-00i.txt