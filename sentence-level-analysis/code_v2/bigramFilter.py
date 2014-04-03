import sys
from replaceExpand import *
from collections import defaultdict

if __name__ == '__main__':

    """create emoticons dictionary"""
    f=open("emoticonsWithPolarity.txt",'r')
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
    f=open("acronym_tokenised.txt",'r')
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
    f=open("stopWords.txt", "r")
    for line in f:
        if line:
            line=line.strip(specialChar).lower()
            stopWords[line]=1
    f.close()

    biDict={}
 
    f=open(sys.argv[1],'r')
    for i in f:
        if i:
            i=i.split('\t')
            tweet=i[1].split()
            token=i[2].split()
            label=i[3].strip()
            if tweet:
                tweet, token, count1, count2 = preprocesingTweet1(tweet, token, emoticonsDict, acronymDict)
                tweet,token=preprocesingTweet2(tweet, token, stopWords)
                tweet=[i.strip(specialChar).lower() for i in tweet]
                tweet=[i for i in tweet if i]
                for i in range(len(tweet)-1):
                    phrase=tweet[i]+' '+tweet[i+1]
                    if phrase not in biDict:
                        biDict[phrase]=[0,0,0]
                    biDict[phrase][eval(label)]+=1
    f.close()
    biModel=[]
    for i in biDict.keys():
        count=reduce(lambda x,y:x+y,biDict[i])
        if count>=10:
            count=count*1.0
            pos=biDict[i][positive]/count
            neg=biDict[i][negative]/count
            neu=biDict[i][neutral]/count
            if pos>0.9 or neg>0.9 or neu > 0.9:
                l=[i,pos,neg,neu,count]
                biModel.append(l)

    biModel=sorted(biModel,key=lambda x:x[4],reverse=True) 
    for i in biModel:
        print i[0]
