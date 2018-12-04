from bs4 import BeautifulSoup as web
from basic_parser import Parser


class M24_parser(Parser):
    def __init__(self):
        super().__init__("https://www.m24.ru/rss.xml")

    def grab(self, url):
        content = web(self.get_content(url), "html.parser")
        obj = {}
        obj["title"] = content.select(
            ".b-material-before-body__data > h1"
        )[0].text
        obj["image"] = content.select(
            ".b-material-incut-m-image > img"
        )[0]["src"]
        obj["content"] = list(
            map(
                lambda x: x.text,
                content.select(".js-mediator-article > p")
            )
        )
        return obj


if __name__ == "__main__":
    m24 = M24_parser()
    news = m24.news()
    print(news)
    url = news[0]["link"]
    print(url)
    data = m24.grab(url)
    print(data)
