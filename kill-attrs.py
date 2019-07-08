from bs4 import BeautifulSoup
from os import listdir, curdir
from os.path import isfile

def remove_attrs(soup):
  for tag in soup.findAll(True):
    tag.attrs = {
      "href": tag.get('href'),
      "src": tag.get('src')
    }
    if not tag.get('href'):
      del tag['href']
    if not tag.get('src'):
      del tag['src']
  return soup

files = filter(isfile, listdir(curdir))

for f in files:
  if f.endswith('.html'):
    with open(f, 'r') as html_file:
      html = html_file.read()
      soup = BeautifulSoup(html, 'html.parser')
      stripped = remove_attrs(soup)
    with open(f, 'w') as html_file:
      html_file.write(stripped.prettify())
