import requests
from bs4 import BeautifulSoup
import csv
import requests

url = "https://quotes.toscrape.com/"
response = requests.get(url)

if response.status_code != 200:
    print("Failed to fetch webpage")
    exit()
soup = BeautifulSoup(response.text, "html.parser")
quotes_data = []

quotes = soup.find_all("div", class_="quote")

for quote in quotes:
    text = quote.find("span", class_="text")
    author = quote.find("small", class_="author")
    tags = quote.find("div", class_="tags")

    quote_text = text.get_text() if text else "N/A"
    author_name = author.get_text() if author else "N/A"

    tag_list = []
    if tags:
        for tag in tags.find_all("a"):
            tag_list.append(tag.get_text())

    quotes_data.append([
        quote_text,
        author_name,
        ", ".join(tag_list)
    ])
with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author", "Tags"])
    writer.writerows(quotes_data)

print("Data successfully saved to quotes.csv")


