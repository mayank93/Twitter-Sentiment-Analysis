"""This code extracts the features and returns the features"""
from preProcessing import *
from featureExtractor import *
#from probablityModel import *
import sys
from collections import defaultdict
from svmutil import *

if __name__ == '__main__':
    
    """check arguments"""
    if len(sys.argv)!= 3:                                                   
        print "Usage :: python main.py ../dataset/finalTrainingInput.txt ../dataset/finalTestingInput"
        sys.exit(0)

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
#    for i  in emoticonsDict.keys():
 #       print i,emoticonsDict[i]
    f.close()

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
#            print len(value)-len(token)
            acronymDict[key]=[value,token]
           # print acronymDict[key]
    f.close()
#    for i in acronymDict.keys():
#        print i,acronymDict[i]
    """create stopWords dictionary"""
    stopWords=defaultdict(int)
    f=open("stopWords.txt", "r")
    for line in f:
        if line:
            line=line.strip(specialChar).lower()
            stopWords[line]=1
    f.close()

    """extract featureList for n-gram model"""
    """  f=open(sys.argv[1],'r')
    f1=open('t1.txt','w')
    count=0
    list1=[]
    for i in f:
        i=i.split('\t')
        count=count+1
        start=int(i[0].strip())
        end=int(i[1].strip())
        tweet=i[3].split()
        token=i[4].split()
        if len(tweet)<=end:
            #list1.append(str(count))
            f1.write(str(count)+'\n')
            #f1.write("".join(list1))
    f1.close()
    f.close()"""
    
    f=open(sys.argv[1],'r')
    featureList=[]
    for i in f:
    	if i:
            
            i=i.split('\t')
            start=int(i[0].strip())
            end=int(i[1].strip())
            tweet=i[3].split()
            token=i[4].split()
            tweet,token,start,end=preprocesingTweet1(tweet, token,start,end, emoticonsDict, acronymDict,stopWords)
            
 
            for j in range(len(tweet)):
                featureList.extend(tweet)
            phrase="" 
            start=int(start)
            end=int(end)
            length=len(tweet)
        
            for k in range(start,end+1):
                if k < length:
                    phrase=phrase+' '+tweet[k]   
            #print phrase
           
    for i in range(len(featureList)-1):
        featureList.extend([featureList[i]+' '+featureList[i+1]])
    featureList.extend([phrase])
     
    featureList=list(set(featureList))
   
    
    """featureList creadted for n-gram"""

    encode={'positive': 1,'negative': -1,'neutral':0}

    sortedFeatureList = sorted(featureList)
    map = {}
    #count=0
    f=open(sys.argv[1],'r')
    featureVectors=[]
    trainingLabel=[]
    for i in f:
        if i:
            i=i.split('\t')
            start=int(i[0].strip())
            end=int(i[1].strip())
            label=i[2].strip()
            tweet=i[3].split()
            token=i[4].split()
            
            for k in sortedFeatureList:
                map[k] = 0

            if tweet:
                #count=count+1
                tweet,token,start,end=preprocesingTweet1(tweet, token,start,end,emoticonsDict, acronymDict,stopWords)
                trainingLabel.append(encode[label])
                #vector,start,end=findFeatures(tweet, token,start,end,stopWords, emoticonsDict, acronymDict)
                vector = []
                for word in tweet:
                    if word in map:
                         map[word] = map[word]+1
                values = map.values()
                vector.extend(values)
                featureVectors.append(vector)
  
                #print count
        
    f.close()

    print "Feature Vectors Created....."
    """Feed the feature vector to svm to create model"""
    print "Creating SVM Model"
    model= svm_train(trainingLabel,featureVectors)
    print "Model created. Saving..."
    """Save model"""
    svm_save_model('sentimentAnalysis.model', model)
    print "Model Saved. Proceed to test..."
    """for each new tweet create a feature vector and feed it to above model to get label"""


    testingLabel=[]
    f=open(sys.argv[2],'r')
    featureVectors=[]
    for i in f:
        if i:
            i=i.split('\t')
            start=int(i[0].strip())
            end=int(i[1].strip())
            label=i[2].strip()
            tweet=i[3].split()
            token=i[4].split()
            for k in sortedFeatureList:
                map[k] = 0
            if tweet:
                tweet,token,start,end=preprocesingTweet1(tweet, token,start,end,emoticonsDict, acronymDict,stopWords)
                testingLabel.append(encode[label])
                #vector,start,end=findFeatures(tweet, token,start,end, stopWords, emoticonsDict, acronymDict)
                #featureVectors.append(vector)
                for word in tweet:
                    if word in map:
                        map[word] = map[word]+1
                values = map.values()
                vector = []
                vector.extend(values)
                featureVectors.append(vector)
    f.close()
    print "Feature Vectors of test input created. Calculating Accuracy..."
    predictedLabel, predictedAcc, predictedValue = svm_predict(testingLabel, featureVectors, model)
    print "Finished. The accuracy is:"
    print predictedAcc[0]

  

  
