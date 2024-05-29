from bs4 import BeautifulSoup
import re
import requests

def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    anchors = soup.find_all(class_='discussion-link')
    links = []
    for a in anchors:
        text = a.text.strip()
        if re.search('devops', text, re.IGNORECASE):
            links.append('https://www.examtopics.com' + a['href'])
    return links

def extract_question_number(link):
    nums = re.findall(r'\d+', link)
    if nums:
        return int(nums[-1])
    return 0

links = []
for i in range(1, 130):
    url = f'https://examtopics.com/discussions/google/{i}/'
    print(f'Checking for {url}')
    links += get_links(url)

links.sort(key=extract_question_number)

with open('links.txt', 'w') as f:
    for link in links:
        f.write(link + '\n')
