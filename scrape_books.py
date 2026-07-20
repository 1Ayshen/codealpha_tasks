import requests
from bs4 import BeautifulSoup
import pandas as pd

books_data = []

for page in range(1, 51):

    if page == 1:
        url = "https://books.toscrape.com/"
    else:
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    print(f"Scraping Page {page}...")

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        title = book.find("h3").find("a")["title"]

        price = book.find("p", class_="price_color").get_text()
        price = price.replace("Â£", "").replace("£", "")
        price = float(price)

        rating = book.find("p", class_="star-rating")["class"][1]

        book_info = {
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Page":page
        }

        books_data.append(book_info)

df = pd.DataFrame(books_data)

df.to_csv("books.csv", index=False, encoding="utf-8-sig")

print(f"\nDone! {len(books_data)} books saved successfully.")

