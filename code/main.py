from replaceExpand import *
from featureExtractor import *
from probablityModel import *
import sys
from collections import defaultdict

if __name__ == '__main__':
    # write this in main file
    f=open("emoticonsWithPolarity.txt",'r').read().split('\n')
    emoticonsDict={}
    for i in f:
        if i:
            i=i.split()
            value=i[-1]
            key=i[:-1]
            for j in key:
                emoticonsDict[j]=value

    f=open("acronyn.txt",'r').read().split('\n')
    acronymDict={}
    for i in f:
        if i:
            i=i.split('\t')
            print i
            key=i[0]
            value=i[1]
            acronymDict[key]=value

    stopWords=defaultdict(int)
    f=open("stopWords.txt", "r")
    for line in f:
        if line:
            stopWords[line[:-1]]=1

    f=open(sys.argv[1],'r')
    for line in f:
        if line :
            temp = line.split('\t')
            tweet = temp[0].split(' ')
            print tweet
            token = temp[1].split(' ')
            tweet, token = preprocesingTweet(tweet, token, stopWords, emoticonsDict,acronymDict)
            print tweet
            percentageCapitalised = findCapitalised(tweet)
            print percentageCapitalised

#    print probTraining("finalTrainingInput.txt", stopWords, emoticonsDict)
