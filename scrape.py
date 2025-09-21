#request=>get data from web (html,json xml)

import requests  # type: ignore
from bs4 import BeautifulSoup # type: ignore

url="https://books.toscrape.com/"


def scrape_books(url):
    response= requests.get(url)
    # print(response.status_code)

    if response.status_code!=200:
        print("failed to retrieve page")
        return
    response.encoding=response.apparent_encoding
    soup=BeautifulSoup(response.text,"html.parser")
    books= soup.find_all("article", class__="product_pod")
    for book in books:
        title=book.h3.a['title']
        price_text=book.find("p",class_='price_color').text
        currency=price_text[0]
        price=float(price_text[1:])
        all_books.append( # type: ignore
            {
                "title":title
                "currency":currency,
                "price":price,
            }
        )
    return all_books
    

books=scrape_books(url)
with open("books.json","w",encoding='utf-8')as f:
    import json
    json.dump(books,f,indent=4,ensure_ascii=False)

