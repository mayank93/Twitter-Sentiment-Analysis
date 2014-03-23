"""This code extracts the features and returns the features"""
from replaceExpand import *
from featureExtractor import *
from probablityModel import *
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

    """create Unigram Model"""
    print "Creating Unigram Model......."
    polarityDictionary = probTraining(sys.argv[1], stopWords, emoticonsDict, acronymDict)
    print "Unigram Model Created"
    
    """write the polarityDictionary"""
    data=[]
    for key in polarityDictionary:
        data.append(key+'\t'+str(polarityDictionary[key][positive])+'\t'+str(polarityDictionary[key][negative])+'\t'+str(polarityDictionary[key][neutral]))
    f=open('polarityDictionary.txt','w')
    f.write('\n'.join(data))
    f.close()
    

    
    """Create a feature vector of training set """
    print "Creating Feature Vectors....."
    encode={'positive': 1,'negative': -1,'neutral':0}
    trainingLabel=[]
    f=open(sys.argv[1],'r')
    featureVectors=[]
    for i in f:
        if i:
            i=i.split('\t')
            tweet=i[1].split()
            token=i[2].split()
            label=i[3].strip()
            tweet,token,count=preprocesingTweet(tweet, token, stopWords, emoticonsDict, acronymDict)
            print tweet
            if tweet:
                trainingLabel.append(encode[label])
                featureVectors.append(findFeatures(tweet, token, polarityDictionary, count))
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
            tweet=i[1].split()
            token=i[2].split()
            label=i[3].strip()
            tweet,token,count=preprocesingTweet(tweet, token, stopWords, emoticonsDict, acronymDict)
#            print tweet
            if tweet:
                testingLabel.append(encode[label])
                featureVectors.append(findFeatures(tweet, token, polarityDictionary, count))
    f.close()
    print "Feature Vectors of test input created. Calculating Accuracy..."
    predictedLabel, predictedAcc, predictedValue = svm_predict(testingLabel, featureVectors, model)
    print "Finished. The accuracy is:"
    print predictedAcc[0]
