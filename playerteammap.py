from bs4 import BeautifulSoup
import json
import requests
import re
response = requests.get('http://www.cricbuzz.com/cricket-series/2676/indian-premier-league-2018/squads')
soup = BeautifulSoup(response.text, 'html.parser')
content=soup.find(id="page-wrapper")

templist=['Chennai Super Kings',
'Royal Challengers Bangalore',
'Kings XI Punjab',
'Rajasthan Royals',
'Delhi Daredevils',
'Mumbai Indians', 
'Sunrisers Hyderabad',
'Kolkata Knight Riders']

teams=[]
x=0
for a in content.contents[7].find_all('a'):
    if a.string:
        #print(a.string)
        if a.string!='More Stats':
            #print(a.string)
            if a.string in templist:
                #print(a.string)
                if  x>0:
                    teams.append(newteam)
                    #print(newteam)       
                x=x+1
                newteam={} #make new team object here
                newteam['name']=a.string #assigning name to the team
                #newteam['captain']=""
                newteam['squad']=[]
            else:
                newplayer={}
                newplayer['name']=a.string
                #newplayer['alias']=[]
                #print(a.string)
                newteam['squad'].append(newplayer)        
        else:
            teams.append(newteam)
print(teams)