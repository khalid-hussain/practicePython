'''
Required modules:
    pip install requests
    pip install beautifulsoup4
'''

import requests
from bs4 import BeautifulSoup

base_url = "http://www.nytimes.com"
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

with open('21-writeToFileOutput.txt', 'w') as open_file:
    for story_heading in soup.find_all(class_="story-heading"):
        if story_heading.a:
            open_file.write(story_heading.a.text.replace("\n", " ").strip())
            # print(story_heading.a.text.replace("\n", " ").strip())
        else:
            open_file.write(story_heading.contents[0].strip())
            # print(story_heading.contents[0].strip())
