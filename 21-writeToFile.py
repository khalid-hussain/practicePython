import requests
from bs4 import BeautifulSoup

base_url = "http://www.nytimes.com"
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

open_file = open("21-writeToFileOutput.txt", "w")

for story_heading in soup.find_all(class_="story-heading"):
    if story_heading.a:
        open_file.write(story_heading.a.text.replace("\n", " ").strip())
        # print(story_heading.a.text.replace("\n", " ").strip())
    else:
        open_file.write(story_heading.contents[0].strip())
        # print(story_heading.contents[0].strip())

open_file.close()
