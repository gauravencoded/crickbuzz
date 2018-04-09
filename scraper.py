from bs4 import BeautifulSoup
import json
import requests
response = requests.get('http://www.cricbuzz.com/live-cricket-scorecard/20061/mi-vs-csk-1st-match-indian-premier-league-2018')
soup = BeautifulSoup(response.text, 'html.parser')
#functionalities to get data about inning 1

first_inning_result=[]
inning1=soup.find(id='innings_1')
child=inning1.contents
print("#batting firsh inning")
i=5 #because records start from 5th row
while i<len(child[1].contents):
    if child[1].contents[i].contents[1].string!='Extras':
        first_inning={}
        first_inning['name']=child[1].contents[i].contents[1].find('a').string
        first_inning['wicketstyle']=child[1].contents[i].contents[3].find('span').string
        first_inning['runs']=child[1].contents[i].contents[5].string
        first_inning['balls']=child[1].contents[i].contents[7].string
        first_inning['fours']=child[1].contents[i].contents[9].string
        first_inning['sixes']=child[1].contents[i].contents[11].string
        first_inning['strikerate']=child[1].contents[i].contents[13].string
        first_inning_result.append(first_inning) #contains the batting scorecard
    else:
        break
    i=i+2;
print(first_inning_result)
#batting score is prepared for first inning stored in : first_inning_result


#starting to prepare catches and runout score
print("#starting fitness data")
fitness_performance=[]
for a in first_inning_result:
    if a['wicketstyle']!='batting' and a['wicketstyle']!='not out':
        wstyle=a['wicketstyle'].split(' ')
        if wstyle[0]!='lbw':
            playfitness={}
            playfitness['contribution']=wstyle[0]
            playfitness['name']=wstyle[1]
            fitness_performance.append(playfitness)

print(fitness_performance)
#catch, runout score calculation completed



print("#bowling first inning")
first_inning_bowl_result=[]
i=3 #because records start from 3th row
while i<len(child[6].contents):
    first_inning_bowl={}
    first_inning_bowl['name']=child[6].contents[i].contents[1].find('a').string #names
    first_inning_bowl['overs']=child[6].contents[i].contents[3].string#overs
    first_inning_bowl['maiden']=child[6].contents[i].contents[5].string#maiden
    first_inning_bowl['runsgiven']=child[6].contents[i].contents[7].string#run
    first_inning_bowl['wickets']=child[6].contents[i].contents[9].string#wicket
    first_inning_bowl['noballs']=child[6].contents[i].contents[11].string#nb
    first_inning_bowl['wideballs']=child[6].contents[i].contents[13].string#wd
    first_inning_bowl['economy']=child[6].contents[i].contents[15].string#eco
    first_inning_bowl_result.append(first_inning_bowl)
    i=i+2;
print(first_inning_bowl_result)

#functionalities to get data about inning 1
second_inning={}
second_inning_bowl={}
inning2=soup.find(id='innings_2')
if inning2:
    print("batting second innning")
    child=inning2.contents
    i=5 #because records start from 5th row
    second_inning_result=[]
    while i<len(child[1].contents):
        if child[1].contents[i].contents[1].string!='Extras':
            second_inning={}
            second_inning['name']=child[1].contents[i].contents[1].find('a').string
            second_inning['wicketstyle']=child[1].contents[i].contents[3].find('span').string
            second_inning['runs']=child[1].contents[i].contents[5].string
            second_inning['balls']=child[1].contents[i].contents[7].string
            second_inning['fours']=child[1].contents[i].contents[9].string
            second_inning['sixes']=child[1].contents[i].contents[11].string
            second_inning['strikerate']=child[1].contents[i].contents[13].string
            second_inning_result.append(second_inning)#print(json.dumps(second_inning))
        else:
            break
        i=i+2;

    print(second_inning_result)

    #starting to prepare catches and runout score
    print("#starting fitness data")
    fitness_performance=[]
    for a in second_inning_result:
        if a['wicketstyle']!='batting' and a['wicketstyle']!='not out':
            wstyle=a['wicketstyle'].split(' ')
            if wstyle[0]!='lbw':
                playfitness={}
                playfitness['contribution']=wstyle[0]
                playfitness['name']=wstyle[1]
                fitness_performance.append(playfitness)

    print(fitness_performance)
    #catch, runout score calculation completed









    print("bowling second innning")
    #print(child[6])
    second_inning_bowl_result=[]
    i=3
    while i<len(child[6].contents):
        second_inning_bowl={}
        second_inning_bowl['name']=child[6].contents[i].contents[1].find('a').string #names
        second_inning_bowl['overs']=child[6].contents[i].contents[3].string#overs
        second_inning_bowl['maiden']=child[6].contents[i].contents[5].string#maiden
        second_inning_bowl['runsgiven']=child[6].contents[i].contents[7].string#run
        second_inning_bowl['wickets']=child[6].contents[i].contents[9].string#wicket
        second_inning_bowl['noballs']=child[6].contents[i].contents[11].string#nb
        second_inning_bowl['wideballs']=child[6].contents[i].contents[13].string#wd
        second_inning_bowl['economy']=child[6].contents[i].contents[15].string#eco
        second_inning_bowl_result.append(second_inning_bowl)
        i=i+2
    print(second_inning_bowl_result)
else:
    print("No data for second inning");