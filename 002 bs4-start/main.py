from bs4 import BeautifulSoup
import requests

# with open("website.html", 'r', encoding="utf-8") as file:
#     contents = file.read()
# #print(contents)
# soup = BeautifulSoup(contents, 'html.parser')
#
# [print(items.string) for items in soup.find_all('li')]
# [print(anchor_tags.get('href')) for anchor_tags in soup.find_all('a')]
# # print(soup.h1.string)
# # print(soup.p)
# print(soup.find('h1', id='name'))

response = requests.get("https://quotes.toscrape.com/")
quote_webpage = response.text

soup = BeautifulSoup(quote_webpage, 'html.parser')
first_quote = soup.find('span', class_='text')
author = soup.find('small', class_='author')
# print(first_quote.get_text())
# print(author.get_text())

titles = [
    "I refactored my 2010 spaghetti code",
    "Lessons from building a CLI startup",
    "How I tamed CSS grid and lived to tell",
    "Migrating legacy APIs in 3 days"
]

urls = [
    "https://devblog.example.com/refactoring-journey",
    "https://devblog.example.com/cli-startup",
    "https://devblog.example.com/css-grid-survival",
    "https://devblog.example.com/api-migration"
]

upvotes = [75, 223, 98, 156]

biggest_upvote = upvotes.index(max(upvotes))
print(titles[biggest_upvote])
print(urls[biggest_upvote])
print(upvotes[biggest_upvote])
#
#
# print(titles)
# print(urls)
# print(upvotes)

