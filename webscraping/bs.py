# from bs4 import BeautifulSoup
# import lxml

# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "lxml")

# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.prettify)

# # print(soup.p)

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)
# print()

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)


from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

print(response.text)

