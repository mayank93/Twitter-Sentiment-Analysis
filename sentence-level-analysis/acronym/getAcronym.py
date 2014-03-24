import sys
from bs4 import BeautifulSoup

data=open(sys.argv[1],'r').read()
soup = BeautifulSoup(data)
acr = soup.findAll('strong')
acr=[i.string for i in acr]
abr = soup.findAll('dd')
abr=[i.string for i in abr]
size=len(abr)
for i in range(size):
    try:
        print str(acr[i])+'\t'+str(abr[i])
    except:
        print str(acr[i])
