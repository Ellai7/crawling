import requests
res = requests.get("http://naver.com")

res.raise_for_status()
print(len(res.text))

with open("test.html", "w", encoding="utf8") as f:
    f.write(res.text)  