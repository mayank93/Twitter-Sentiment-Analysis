from replaceExpand import *
from featureExtractor import *
from probablityModel import *
import sys
from collections import defaultdict
trainFile="finalTrainingInput.txt"

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
            key=i[0].lower()
            value=i[1].lower()
            acronymDict[key]=value

    stopWords=defaultdict(int)
    f=open("stopWords.txt", "r")
    for line in f:
        if line:
            line=line.strip('\n \t\r').lower()
            stopWords[line]=1

    print "Creating Unigram Model......."
    polarityDictionary = probTraining(trainFile, stopWords, emoticonsDict, acronymDict)
    print "Unigram Model Created"
    
    """Create a feature vector of training set """
    print "Creating Feature Vectors....."
    f=open(trainFile,'r')
    featureVectors=[]
    for i in f:
        if i:
            i=i.split('\t')
            tweet=i[1].split()
            token=i[2].split()
            label=i[3].strip()
            tweet,token=preprocesingTweet(tweet, token, stopWords, emoticonsDict, acronymDict)
            if tweet:
                featureVectors+=list(findFeatures(tweet, token, polarityDictionary))

    print "Feature Vectors Created....."

    """Feed the feature vector to svm to create model"""
    
    """for each new tweet create a feature vector and feed it to above model to get label"""

    f=open(sys.argv[1],'r')
    for line in f:
        temp = line.split('\t')
        tweet = temp[0].split(' ')
        print tweet
        token = temp[1].split(' ')
        tweet, token = preprocesingTweet(tweet, token, stopWords, emoticonsDict,acronymDict)
        print tweet
        featureVector = findFeatures(tweet, token, polarityDictionary)
        print featureVector
        break
#    print probTraining("finalTrainingInput.txt", stopWords, emoticonsDict)
