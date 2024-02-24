import requests
from bs4 import BeautifulSoup
import csv


url="https://www.indiatoday.in/"

page=requests.get(url)

soup=BeautifulSoup(page.content,'html.parser')
print(soup.prettify())

headline=[]
headlines=soup.findAll('div',class_="B1S3_content__wrap__9mSB6")
story=[]
newstory=soup.findAll('div',class_="B1S3_story__shortcont__inicf")


for i in headlines:
    j=i.a['title']
    headline.append(j)

for i in newstory:
    j=i.p.text
    story.append(j)
    

    
with open('hl.csv', 'w', newline='', encoding='utf-8') as csv_file:
    write = csv.writer(csv_file)
    
   
    write.writerow(['Headline','story'])

  
    for i,j in zip(headline,story):
        write.writerow([i, ''])  
        write.writerow(['', j])  
