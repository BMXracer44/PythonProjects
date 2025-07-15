from lxml import html
import requests

url = 'https://google.com'
response = requests.get(url)
tree = html.fromstring(response.content)

#Extract all link texts
link_titles = tree.xpath('//a/text()')

for title in link_titles:
    print(title)
