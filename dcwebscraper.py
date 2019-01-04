#Import Libraries: requests, BeautifulSoup, inflection

import requests
from bs4 import BeautifulSoup
import inflection

#Send request; suggest input variable instead of hard code

r = requests.get('http://www.dailysmarty.com/topics/python')

#Parse returned request

webtext = BeautifulSoup(r.text, "html.parser")

#Import Library: re

import re

#Find links with posts

for link in webtext.find_all(href=re.compile("posts")):
    
    weburls = link.get('href')

#Strip /posts/ from list

    weburls = weburls[7:]

#Make 'em pretty, print output

    pretty_titles = inflection.titleize(weburls)

    print(pretty_titles)