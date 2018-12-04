import requests
import xml.etree.ElementTree as xml


class Parser():
    def __init__(self, url):
        self.url = url
        self.encoding = "utf-8"

    def get_content(self, url, encoding=None):
        res = requests.get(url)
        if encoding is not None:
            res.encoding = encoding
        return res.text

    def news(self, limit=3, root=None):
        self.root = xml.fromstring(self.get_content(self.url, self.encoding))
        if root is None:
            root = self.root
        body = root[0]
        items = body.findall("item")[:limit]
        res = []
        for item in items:
            obj = {}
            if item.find("title") is not None:
                obj["title"] = item.find("title").text
            if item.find("link") is not None:
                obj["link"] = item.find("link").text
            if item.find("description") is not None:
                obj["desc"] = item.find("description").text.strip()
            if item.find("pubDate") is not None:
                obj["published"] = item.find("pubDate").text
            res.append(obj)
        return res

    def grab(self, url):
        pass


if __name__ == "__main__":
    s = Parser("http://lenta.ru/rss")
    news = s.news()
    url = news[0]["link"]
