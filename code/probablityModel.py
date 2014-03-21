from replaceExpand import *
from senti_classifier import senti_classifier


def probTraining(trainFile, stopWords, emoticonsDict, acronymDict):
    """trainFile is a file which contain the traind data is following format
    tokenizedTweet\tpos\tlabel\n it return the dictonary comtaining the prob of word being positive, negative, neutral"""

    wordProb={}
    tweetCount=[0,0,0,0]
    f=open(trainFile,'r') 
    for i in f:
        if i:
            i=i.split('\t')
            tweet=i[1].split()
            token=i[2].split()
            label=i[3].strip()
            tweet,token=preprocesingTweet(tweet, token, stopWords, emoticonsDict, acronymDict)
            for i in tweet:
                i=i.lower()
                if i not in wordProb:
                    wordProb[i]=[0.0,0.0,0.0,0]
                wordProb[i][eval(label)]=wordProb[i][eval(label)]+1.0
                wordProb[i][total]=wordProb[i][total]+1.0
                tweetCount[eval(label)]=tweetCount[eval(label)]+1
                tweetCount[total]=tweetCount[total]+1

    for i in wordProb.keys():
        
        posScore, negScore = senti_classifier.polarity_scores([i])
        wordProb[i][positive]=( ( ( wordProb[i][positive]*1.0 ) / wordProb[i][total] ) + posScore ) / 2.0
        wordProb[i][negative]=( ( ( wordProb[i][negative]*1.0 ) / wordProb[i][total] ) + negScore ) / 2.0
        wordProb[i][neutral]=(wordProb[i][neutral]*1.0)/wordProb[i][total]

    return wordProb
