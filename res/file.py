import requests 
from bs4 import BeautifulSoup 
import json
import re

URL = "https://sh.58.com/qzyewu/"
r = requests.get(URL) 
# re.sub(r'</?\w+[^>]*>', '', r)
soup = BeautifulSoup(r.content.decode("utf-8"), 'html5lib')    

resume = []
s='&#xe496;&#xeaa1;/&#xe08f;&#xe868;'
k = s.replace(';', '').replace('&#x', r'\u00').encode('utf-8').decode('unicode-escape')
print(k)  
table = soup.find('div', attrs = {'class':'tablist'}) 
for row in table.findAll('dl'):
    res = {}
    temp=row.find('dt')
    res['qiuzhixiang'] = temp.find('a', attrs={'class': 'fl'}).string
    r = row.find('dd', attrs = {'class':'w48 stonefont'}).text
    # r = re.sub(r'&#x([A-F0-9]{2});', r'&#x00\1;', r)
    res['gender'] = r.replace(';', '').replace('&#x', r'\u00').encode('utf-8').decode('unicode-escape')
    print(res['gender'])
    res['age']=row.find('dd', attrs = {'class':'w60 stonefont'}).string
    res['rep']=row.find('dd', attrs = {'class':'w108'}).string
    resume.append(res)
filename = 'resume.json'
with open(filename, 'w') as json_file:
    json.dump(resume, json_file)
    

