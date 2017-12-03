# -*- coding: utf-8 -*-

# simple commandline library for getting the top 10 request for hackers news
# author = "shammah Agwor"
# date = "novemeber 2017

# re = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
# requests.get('https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'

import requests
import json

url_array = []


def get(url):
    """send get request to the given url
    """
    req = requests.get(url)
    req = req.text
    return req


def toArray(reqObject):
    """covert the request response from hn api
        to  an array
    """
    req = reqObject
    req = json.loads(req)
    return req


def firstTen(anArray):
    resArray = []
    """
    take the first ten item from an array and return a new array
    of the ten items
    
    """
    for i in range(0, 10):
        resArray.append(anArray[i])
    return resArray


def getStories(anArray):
    """
    gets the hn stories from their api

    :param anArray:
    :return: json array
    """
    arr = anArray
    storiesArray = []

    for item in arr:
        story = get('https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'.format(item))
        storiesArray.append(json.loads(story))

    return storiesArray


def displayer(storiesArray):
    """
    displays the hn stories on your commandline
    :param storiesArray:
    :return: NOne
    """
    Arr = storiesArray
    for i in range(0,10):
        print()
        print(Arr[i]["title"],end ="")
        print("\t points =",  Arr[i]["score"],end="")
        print("\t  By =",Arr[i]["by"])
        print(Arr[i]["url"])
        print("****************************************************************")

if  __name__ == '__main__':
    print("Getting the stories.........................")
    hnstories = firstTen(toArray(get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')))
    hnstories =getStories(hnstories)
    displayer(hnstories)
