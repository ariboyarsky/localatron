import requests
from bs4 import BeautifulSoup as bs

class NBCLocalScrape:

    def get_article_urls(self, url, page):
        articles = []
        r = requests.get(url + str(page))

        soup = bs(r.text, "html5lib")

        headlines = soup.find_all("h3", attrs={"id": lambda L: L and L.startswith('headline')})

        for headline in headlines:
            links = headline.find_all("a")
            for link in links:
                articles.append(link.get('href'))

        return articles

    def get_article_text(self, url):
        r = requests.get(url)

        soup = bs(r.text, "html5lib")
        article = soup.find("div", attrs={"class":"articleText"})
        text = ""
        if article is not None:
            texts = article.find_all("p", attrs={"class":"paragraph"})
            for t in texts:
                text += str(t.text) + " "
            return text
        else:
            return ""


