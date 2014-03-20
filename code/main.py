from replaceExpand import *
from featureExtractor import *
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
    acronymDict={}

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

            tweet, token = preprocesingTweet(tweet, token, stopWords, emoticonsDict)
            print tweet
            percentageCapitalised = findCapitalised(tweet)
            print percentageCapitalised

    probTraining("finalTrainingInput.txt", stopWords, emoticonsDict)
