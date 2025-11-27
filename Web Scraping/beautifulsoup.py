from bs4 import BeautifulSoup
import pandas as pd
import requests

# def fetch_webpage(url: str) ->str:
#   response = requests.get(url)
#   response.raise_for_status
#   return response.text
# url = "https://books.toscrape.com/catalogue/page-1.html"

with open('books.html', "r") as f:
  content = f.read()

soup = BeautifulSoup(content, "html.parser")

books = soup.find_all('article', class_='product_pod')

list_books: list[str] = []
for book in books:
  title = book.find("h3").find("a")['title']
  price = book.select_one("p.price_color").text.strip()[-6:]
  # availability = book.find('p', class_="instock availability").text.strip()
  rating = book.find("p", class_="star-rating")['class'][1]
  
  list_books.append([title, price, rating])
  # print(f"Book title: {title}\nPrice: {price}\nAvailability: {availability}\n")

# print(list_books)
books_data = pd.DataFrame(list_books, columns=["Title", 'Price', "Rating(out of 5)"])
# print(books_data)
books_data.to_csv("books_scraped.csv", index=False)