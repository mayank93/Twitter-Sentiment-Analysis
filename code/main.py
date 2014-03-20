from replaceExpand import *
from featureExtractor import *
from probablityModel import *
import sys
from collections import defaultdict

if __name__ == '__main__':
    # write this in main file
    if len(sys.argv)!= 2:                                                                               #check arguments
        print "Usage :: python main.py ../dataset/finalTrainingInput.txt"

    f=open("emoticonsWithPolarity.txt",'r').read().split('\n')
    emoticonsDict={}
    for i in f:
        if i:
            i=i.split()
            value=i[-1]
            key=i[:-1]
            for j in key:
                emoticonsDict[j]=value

    f=open("acronym.txt",'r').read().split('\n')
    acronymDict={}
    for i in f:
        if i:
            i=i.split('\t')
            key=i[0]
            value=i[1]
            acronymDict[key]=value

    stopWords=defaultdict(int)
    f=open("stopWords.txt", "r")
    for line in f:
        if line:
            stopWords[line[:-1]]=1

    print "Hello"
    polarityDictionary = probTraining(sys.argv[1], stopWords, emoticonsDict, acronymDict)
    print "Unigram Model Created"
    f=open(sys.argv[1],'r')
    for line in f:
        temp = line.split('\t')
        tweet = temp[0].split(' ')
        print tweet
        token = temp[1].split(' ')
        tweet, token = preprocesingTweet(tweet, token, stopWords, emoticonsDict,acronymDict)
        print tweet
        #featureVector = featureExtractor(tweet, token, polarityDictionary)
        break
#    print probTraining("finalTrainingInput.txt", stopWords, emoticonsDict)
