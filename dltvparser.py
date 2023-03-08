import requests
import re
from bs4 import BeautifulSoup as BS

link = "https://ru.dltv.org/matches/403256"

def getTeamComposition(url):
    x = []
    y = []

    reqUrl = requests.get(url)

    htmlParsed = BS(reqUrl.content, "lxml")
    radiantpick = htmlParsed.select(".picks__new-picks__picks.radiant .items .pick")
    direpick = htmlParsed.select(".picks__new-picks__picks.dire .items .pick")

    for item in radiantpick:
        if item.attrs['data-tippy-content'] == "Anti-Mage":
            x.append("Anti_Mage")
        else:
            x.append(item.attrs['data-tippy-content'])

    for item in direpick:
        if item.attrs['data-tippy-content'] == "Anti-Mage":
            y.append("Anti_Mage")
        else:
            y.append(item.attrs['data-tippy-content'])

    for i, j in enumerate(x):
        x[i] = j.replace(" ", "_")          
        
    for i, j in enumerate(y):
        y[i] = j.replace(" ", "_")
       
    return x, y    
    

def getTeamTag(url):
    x = []
    y = []

    reqUrl = requests.get(url)

    htmlParsed = BS(reqUrl.content, "lxml")

    bothTeamsTag = htmlParsed.select(".team .team__title-name .name")
    for i in bothTeamsTag:
        x.append(i.string)

    return x
    



if __name__ == '__main__':
    # print(*getTeamComposition(link))
    print(getTeamTag(link))

    