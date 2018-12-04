from bs4 import BeautifulSoup as web
from basic_parser import Parser


class Interfax_parser(Parser):
    def __init__(self):
        super().__init__("http://www.interfax.ru/rss.asp")
        self.site_encoding = "windows-1251"

    def grab(self, url):
        content = web(self.get_content(url, self.site_encoding), "html.parser")
        obj = {}
        if content.select(".textMTitle")[0]:
            obj["title"] = content.select(".textMTitle")[0].text
        if content.select(".inner > img"):
            obj["image"] = "{}{}".format(
                "https://www.interfax.ru/",
                content.select(".inner > img")[0]["src"]
            )
        print(len(content.select(".at > article > p")))
        if content.select(".at > article > p"):
            obj["content"] = list(
                map(
                    lambda x: x.text,
                    content.select(".at > article > p")
                )
            )
        return obj


if __name__ == "__main__":
    inter = Interfax_parser()
    news = inter.news()
    print(news)
    url = news[0]["link"]
    print(url)
    data = inter.grab(url)
    print(data)
