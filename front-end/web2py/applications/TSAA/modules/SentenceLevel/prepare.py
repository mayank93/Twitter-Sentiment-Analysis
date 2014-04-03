from replaceExpand import *
from collections import defaultdict

def loadDictionary(emoticonsFile, acronymFile, stopWordsFile):
    """create emoticons dictionary"""
    f=open(emoticonsFile,'r')
    data=f.read().split('\n')
    emoticonsDict={}
    for i in data:
        if i:
            i=i.split()
            value=i[-1]
            key=i[:-1]
            for j in key:
                emoticonsDict[j]=value
    f.close()

    #print emoticonsDict

    """create acronym dictionary"""
    f=open(acronymFile,'r')
    data=f.read().split('\n')
    acronymDict={}
    for i in data:
        if i:
            i=i.split('\t')
            word=i[0].split()
            token=i[1].split()[1:]
            key=word[0].lower().strip(specialChar)
            value=[j.lower().strip(specialChar) for j in word[1:]]
            acronymDict[key]=[value,token]
    f.close()

    #print acronymDict

    """create stopWords dictionary"""
    stopWords=defaultdict(int)
    f=open(stopWordsFile,'r')
    for line in f:
        if line:
            line=line.strip(specialChar).lower()
            stopWords[line]=1
    f.close()

    return acronymDict,stopWords,emoticonsDict
