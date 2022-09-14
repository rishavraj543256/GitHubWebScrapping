from bs4 import BeautifulSoup as soup
import pandas as pd
import requests
url='https://github.com/collections/programming-languages'
response= requests.get(url)
print(response.text)
page_content=response.text
type(page_content)
data=soup(page_content,'html.parser')
print(type(data))
Developer_Company=[]
for item in Dev_Company:
    Developer_Company.append(item.text.replace('/',''))
print(Developer_Company)
Pro = data.find_all('h1',{'class':'h3 lh-condensed'})
Programming_Lang=[]
for pro_lang in Pro:
    Programming_Lang.append(pro_lang.text.replace('/','').split('\n')[6].strip())
print(Programming_Lang)
Lang=data.find_all('div',{'class':'color-fg-muted mb-2 ws-normal'})
desc=[]
for info in Lang:
    desc.append(info.text)
print(desc)
div_selection='d-flex f6'
repo_tags = data.find_all('div',{'class':div_selection})
len(repo_tags)
stars=repo_tags[0].find_all('a')[0].text.strip()
star=[]
for count in repo_tags:
    count=count.find_all('a')[0].text.strip()
    star.append(count)
print(star)
dict = {'Developer Company': Developer_Company, 'Programming Languages': Programming_Lang, 'Description': desc, 'Stars': star}
df = pd.DataFrame(dict)
df
df.to_csv('file1.csv', index=False)