#!/usr/bin/env python3
import requests
import yaml

configFile = "config.yml"

# save api requests to files
def save(lang, obj):
   with open('languages/'+lang+'.yaml', 'w') as f:
       yaml.dump(obj, f)

def getRepos(lang, order):
    r = requests.get("https://api.github.com/search/repositories?q=%20+language:" + lang + "&sort=stars&order=" + order)
    data = r.json()
    save(lang, data)

def readConfig():
    with open(configFile, 'r') as f:
     data = yaml.load(f, Loader=yaml.FullLoader)
     for lang in data["languages"]:
         getRepos(lang, "desc")

readConfig()