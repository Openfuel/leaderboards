#!/usr/bin/env python3
import requests
import yaml
import json

configFile = "config.yml"

# save api requests to files
def save(name, obj):
   with open('users/'+name+'.yaml', 'w') as f:
       yaml.dump(obj, f)

def printJson(json_object):
    print(json.dumps(json_object, indent=1))
def getUsers(cnf):
    cnf["max_pages"] = int(cnf["max_pages"])
    for x in range(1, cnf["max_pages"]):
        r = requests.get("https://api.github.com/search/users?q=followers:" + str(cnf["min_followers"]) + "&sort=followers&per_page="+ str(cnf["per_page"]))
        data = r.json()
        for user in data["items"]:
            save(user["login"], user)

def readConfig():
    with open(configFile, 'r') as f:
     data = yaml.load(f, Loader=yaml.FullLoader)
    getUsers(data["users"])

readConfig()