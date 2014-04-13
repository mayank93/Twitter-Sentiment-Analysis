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

    uniDict={}
 
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
                for i in tweet:
                    word=i.strip(specialChar).lower()
                    if word:
                        if word not in uniDict:
                            uniDict[word]=[0,0,0]
                        uniDict[word][eval(label)]+=1
    f.close()
    uniModel=[]
    for i in uniDict.keys():
        count=reduce(lambda x,y:x+y,uniDict[i])
        if count>=20:
            count=count*1.0
            pos=uniDict[i][positive]/count
            neg=uniDict[i][negative]/count
            neu=uniDict[i][neutral]/count
            if pos>0.7 or neg>0.7 or neu > 0.7:
                l=[i,pos,neg,neu,count]
                uniModel.append(l)

    uniModel=sorted(uniModel,key=lambda x:x[4],reverse=True) 
    for i in uniModel:
        print i[0]
