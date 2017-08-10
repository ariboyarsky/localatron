# This file will scrape training, tuning, and test data from various news sources
# Note: for now we will limit to only NBC domains to aid in scrapping
import Scrape

# local data
# we will collect 100 articles from each site
local_urls = ['http://www.nbcwashington.com/news/local/?page=',  'http://www.nbcnewyork.com/news/local/?page=',
              "http://www.nbcchicago.com/news/local/?page=", "http://www.nbcphiladelphia.com/news/local/?page="]

# collect first 100 links to an article store in dict based on above url
local_articles = []
i = 1
page = 1

scrapper = Scrape.NBCLocalScrape()

for url in local_urls:
    local_articles.extend(scrapper.get_article_urls(url, page))

    while len(local_articles) < i*100:
        page += 1
        local_articles.extend(scrapper.get_article_urls(url, page))
    i += 1

# print(local_articles)
# output each article to a txt file under training, local-00i.txt
local_data = ""
for article in local_articles:
    # print(article)
    local_data += scrapper.get_article_text("http:" + str(article)) + " "

f = open("data/local.txt", "w")
f.write(local_data)
f.close()


# national data
# collect 220 from each
natl_urls = ["https://www.usnews.com/news/national-news", "http://www.foxnews.com/", "http://www.nbcnews.com/news/us-news",
             "http://www.latimes.com/nation/", "http://www.cnn.com/"]

# collect first 100 links to an article store in dict based on above url
# output each article to a txt file under training, national-00i.txt