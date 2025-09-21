#request=>get data from web (html,json xml)
#git config --global user.name "'"
#git config --global user.email ""
#git init
#git status=>if u want to check what are the status of files
# git diff => if u want to check what are the changes
# git add.
# git commit -m "ur message"
# copy paste the git code from github

#1 change the code 
# 2 git add .
# 3 git commit -m "ur message"
# 4 git push
import json
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
    
    json.dump(books,f,indent=4,ensure_ascii=False)

