import requests
from bs4 import BeautifulSoup

url = 'https://www.hoover.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

# opening a file in write mode
f = open("results/links.txt", "w")
for link in soup.find_all("a"):
   data = link.get('href')
   name = link.text
   f.write(data+" : "+name)
   f.write("\n")
f.close()