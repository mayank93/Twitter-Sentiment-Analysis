from replaceExpand import *
from senti_classifier import senti_classifier

def probTraining(trainFile, stopWords, emoticonsDict):
    """trainFile is a file which contain the traind data is following format
    tokenizedTweet\tpos\tlabel\n"""
    wordCount={}
    tweetCount=[0,0,0,0]
    f=open(trainFile,'r') 
    for i in f:
        if i:
            i=i.split('\t')
            tweet=i[1].split()
            token=i[2].split()
            label=i[3].strip()
            tweet,token=preprocesingTweet(tweet, token, stopWords, emoticonsDict)
            for i in tweet:
                if i not in wordCount:
                    wordCount[i]=[0,0,0]

                wordCount[i][eval(label)]+=1
                wordCount[i][total]+=1
                tweetCount[eval(label)]+=1
                tweetCount[total]+=1
    
    for i in wordCount.keys():
        wordCount[i][positive]=(wordCount[i][positive]*1.0)/wordCount[i][total]
        wordCount[i][negative]=(wordCount[i][negative]*1.0)/wordCount[i][total]
        wordCount[i][neutral]=(wordCount[i][neutral]*1.0)/wordCount[i][total]
    

def probTesting():
    pass
