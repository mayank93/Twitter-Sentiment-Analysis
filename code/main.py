from replaceExpand import *
from featureExtractor import findCapitalised
import sys
from collections import defaultdict

def preprocesingTweet(tweet, token, stopWords, emoticonsDict):

    tweet, token = removeNonEnglishWords(tweet, token)
    print tweet
    tweet, token = removeStopWords(tweet, token, stopWords)
    tweet = replaceEmoticons(emoticonsDict, tweet)
    tweet = replaceRepetition(tweet)
    tweet = replaceNegation(tweet)
    tweet = replaceUrl (tweet, token)
    tweet = replaceHashtag (tweet, token)
    tweet = replaceTarget (tweet, token)

    return tweet,token

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
    #print replaceRepetition("Renewed fighting rooooocks  Syria : An early morning explosion rocked flashpoint city Deir Ezzor Saturday ... http://t.co/zf7AKZMr   V V V ^ , D A N N V N N ^ ^ ^ ~ U")
    #print replaceNegation("Renewed fighting isn't isn't rocks Syria : An early morning explosion rocked flashpoint city Deir Ezzor Saturday ... http://t.co/zf7AKZMr    V V V ^ , D A N N V N N ^ ^ ^ ~ U")
