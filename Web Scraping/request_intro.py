import requests

# Calling 'get' function of requests library

# Saving to a file
for i in range(1,4):
  with open(f'bookstoscrape_page{i}.html', 'w', encoding="utf-8") as f:
    response = requests.get(f"https://books.toscrape.com/catalogue/page-{i}.html")
    f.write(response.text)
    print(f"Page-{i} Downloaded")