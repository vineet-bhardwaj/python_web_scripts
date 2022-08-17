import requests
from bs4 import BeautifulSoup

# List of urls to check
urls = [
"https://www.vox.com/recode/2022/8/17/23310168/facebook-mark-zuckerberg-meta-land-of-the-giants-newsfeed-tom-allison-nick-clegg",
"https://www.vox.com/recode/23297459/axios-facebook-advertising-tech-google-peter-kafka-column",
"https://www.vox.com/2022/7/6/23196899/land-of-the-giants-meta-facebook-mark-zuckerberg-podcast-vox-recode-verge"
]
f = open("results/report.txt", "w")
for url in urls:
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    for meta in soup.find_all("meta"):
        exist_description = 'FALSE'
        if(meta.get('name')=='description'):
           exist_description = 'TRUE'
           f.write(url+" : "+" : META DESCRIPTION : "+ exist_description)
           f.write("\n")