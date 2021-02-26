import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a)
# print(soup.a.attrs)
# print(soup.a["href"])

# print(soup.find( attrs = {"class":"Nbtn_upload"}))

rank1 = soup.find(attrs={"class":"rank01"})
# print(rank1.a)
# print(rank1.next_sibling)
# print(rank1.next_sibling.next_sibling)

#print(rank1.parent)

# rank2 = rank1.find_next_sibling("li")
# rank3 = rank2.find_next_sibling("li")
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="독립일기-66화 새벽의 원룸")
print(webtoon)
