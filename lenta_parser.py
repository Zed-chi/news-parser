from bs4 import BeautifulSoup as web
from basic_parser import Parser


class Lenta_parser(Parser):
    def __init__(self):
        super().__init__("http://lenta.ru/rss")

    def grab(self, url):
        content = web(
            self.get_content(url).replace("&nbsp", ""),
            "html.parser"
        )
        obj = {}
        obj["title"] = content.select(".b-topic__title")[0].text.strip()
        obj["image"] = content.select(".g-picture")[0]["src"]
        obj["content"] = list(
            map(
                lambda x: x.text,
                content.select(".b-text > p")
            )
        )
        return obj


if __name__ == "__main__":
    lenta = Lenta_parser()
    news = lenta.news()
    print(news)
    url = news[0]["link"]
    data = lenta.grab(url)
    print(data)
