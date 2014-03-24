'''on the fly in progress'''
'''Enter tweet in examples-tweet'''
'''get output in tweetTokenised.txt'''

from replaceExpand import *
from featureExtractor import *
from probablityModel import *
import sys
from collections import defaultdict
from svmutil import *

if __name__ == '__main__':    

    """create emoticons dictionary"""
    f=open("emoticonsWithPolarity.txt",'r').read().split('\n')
    emoticonsDict={}
    for i in f:
        if i:
            i=i.split()
            value=i[-1]
            key=i[:-1]
            for j in key:
                emoticonsDict[j]=value

    """create acronym dictionary"""
    f=open("acronym.txt",'r').read().split('\n')
    acronymDict={}
    for i in f:
        if i:
            i=i.split('\t')
            key=i[0].lower()
            value=i[1].lower()
            acronymDict[key]=value

    """create stopWords dictionary"""
    stopWords=defaultdict(int)
    f=open("stopWords.txt", "r")
    for line in f:
        if line:
            line=line.strip('\n \t\r').lower()
            stopWords[line]=1
    f.close()

    """create Polarity Dictionary"""
    polarityDictionary=defaultdict(dict)
    f=open('polarityDictionary.txt','r')
    for line in f:
        words=line.strip().split('\t')
        polarityDictionary[words[0]][positive]= words[1]
        polarityDictionary[words[0]][negative]= words[2]
        polarityDictionary[words[0]][neutral]= words[3]
    f.close()

    """Load Model"""
    print "Loading Model"
    model= svm_load_model('sentimentAnalysis.model')

    f=open('../ark-tweet-nlp-0.3.2/tweetsTokenised.txt','r')
    featureVectors=[]
    for i in f:
        if i:
            i=i.split('\t')
            tweet=i[1].split()
            token=i[2].split()
            tweet,token=preprocesingTweet(tweet, token, stopWords, emoticonsDict, acronymDict)
            if tweet:
                featureVectors.append(findFeatures(tweet, token, polarityDictionary))
                print featureVectors
                predictedLabel, predictedAcc, predictedValue = svm_predict([1], featureVectors, model)
                print predictedLabel
    
