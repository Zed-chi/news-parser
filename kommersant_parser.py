from bs4 import BeautifulSoup as web
from basic_parser import Parser


class Kommersant_parser(Parser):
    def __init__(self):
        super().__init__("http://www.kommersant.ru/RSS/news.xml")
        self.encoding = "windows-1251"
        self.site_encoding = "windows-1251"

    def grab(self, url):
        content = web(self.get_content(url, self.site_encoding), "html.parser")
        obj = {}
        if content.select(".article_name"):
            obj["title"] = content.select(".article_name")[0].text
        if content.select(".article_text_wrapper > p"):
            obj["content"] = list(
                map(
                    lambda x: x.text,
                    content.select(".article_text_wrapper > p")
                )
            )
        return obj


if __name__ == "__main__":
    kom = Kommersant_parser()
    news = kom.news()
    print(news)
    url = news[0]["link"]
    title = news[0]["title"]
    print(title, url)
    data = kom.grab(url)
    print(data)
