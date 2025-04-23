from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>Hello</b>text.</p>", "html.parser")
print(soup.p.b.string)