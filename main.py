from bs4 import BeautifulSoup
import requests
import pandas
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page=requests.get(START_URL)
soup = BeautifulSoup(page.text, "html.parser")
table_tags = soup.find("table")
templist=[]
tableRow=table_tags.find_all('tr')
for i in tableRow:
    td=i.find_all('td')
    row=[j.text.rstrip() for j in td]
    templist.append(row)
star_name=[]
distance=[]
mass=[]
radius=[]
lum=[]
for i in range(1,len(templist)):
    star_name.append(templist[i][1])
    distance.append(templist[3])
    mass.append(templist[5])
    radius.append(templist[6])
    lum.append(templist[7])
df2 = pandas.DataFrame(list(zip(star_name,distance,mass,radius,lum)),columns=['Star_name','Distance','Mass','Radius','Luminosity']) 
print(df2) 
df2.to_csv('bright_stars.csv')
