from pprint import pprint
from interfax_parser import Interfax_parser
from kommersant_parser import Kommersant_parser
from m24_parser import M24_parser
from lenta_parser import Lenta_parser


def get_choice():
    choice = ""
    while choice not in ["1", "2", "3", "4"]:
        choice = input(
"""
Выбери службу->
1.Интерфакс
2.Коммерсант
3.Москва24
4.Лента
(1/2/3/4):""")
    return choice


def get_service(choice):
    if choice is "1":
        service = Interfax_parser()
    elif choice is "2":
        service = Kommersant_parser()
    elif choice is "3":
        service = M24_parser()
    elif choice is "4":
        service = Lenta_parser()
    return service


def main():
    while True:
        choice = get_choice()
        service = get_service(choice)
        news = service.news()
        pprint(news)
        if input("Закончить (д/н): ") == "д":
            break


if __name__ == "__main__":
    main()
    # src = Lenta_parser()
    # news = src.news()
    # pprint(news)
    # url = news[0]["link"]
    # pprint(url)
    # data = src.grab(url)
    # pprint(data)
