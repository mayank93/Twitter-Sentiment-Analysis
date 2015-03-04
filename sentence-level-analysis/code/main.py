"""This code extracts the features and returns the features"""
from featureExtractor import *
from probablityModel import *
import sys
from classifier import *
from prepare import *
from collections import defaultdict
from svmutil import *
#from sklearn import naive_bayes
#from sklearn.externals import joblib

if __name__ == '__main__':
    
    """check arguments"""
    if len(sys.argv)!= 3:                                                   
        print "Usage :: python main.py ../dataset/finalTrainingInput.txt ../dataset/finalTestingInput"
        sys.exit(0)

    acronymDict,stopWords,emoticonsDict = loadDictionary()

    priorScore=dict(map(lambda (k,v): (frozenset(reduce( lambda x,y:x+y,[[i] if i not in acronymDict else acronymDict[i][0] for i in k.split()])),int(v)),[ line.split('\t') for line in open(".//code//AFINN-111.txt") ]))
    
    """create Unigram Model"""
    print "Creating Unigram Model......."
    uniModel=[]
    f=open('.//code//unigram.txt','r')
    for line in f:
        if line:
            line=line.strip('\r\t\n ')
            uniModel.append(line)
    uniModel.sort()

    print "Unigram Model Created"

    print "Creating Bigram Model......."
    biModel=[]
    f=open('.//code//bigram.txt','r')
    for line in f:
        if line:
            line=line.strip('\r\t\n ')
            biModel.append(line)
    biModel.sort()
    print "Bigram Model Created"

    print "Creating Trigram Model......."
    triModel=[]
    f=open('.//code//trigram.txt','r')
    for line in f:
        if line:
            line=line.strip('\r\t\n ')
            triModel.append(line)
    triModel.sort()
    print "Trigram Model Created"
    
    """ polarity dictionary combines prior score """
    polarityDictionary = probTraining(priorScore)


    """write the polarityDictionary"""
    """
    data=[]
    for key in polarityDictionary:
        data.append(key+'\t'+str(polarityDictionary[key][positive])+'\t'+str(polarityDictionary[key][negative])+'\t'+str(polarityDictionary[key][neutral]))
    f=open('polarityDictionary.txt','w')
    f.write('\n'.join(data))
    f.close()
    """
    
    """Create a feature vector of training set """
    print "Creating Feature Vectors....."

    encode={'positive': 1.0,'negative': 2.0,'neutral':3.0}
    trainingLabel=[]
    f=open(sys.argv[1],'r')
    featureVectorsTrain=[]
    for i in f:
        if i:
            i=i.split('\t')
            tweet=i[1].split()
            token=i[2].split()
            label=i[3].strip()
            if tweet:
                vector=[]
                trainingLabel.append(encode[label])
                vector,polarityDictionary=findFeatures(tweet, token, polarityDictionary, stopWords, emoticonsDict, acronymDict)
                uniVector=[0]*len(uniModel)
                for i in tweet:
                    word=i.strip(specialChar).lower()
                    if word:
                        if word in uniModel:
                            ind=uniModel.index(word)
                            uniVector[ind]=1
                vector=vector+uniVector

                biVector=[0]*len(biModel)
                tweet=[i.strip(specialChar).lower() for i in tweet]
                tweet=[i for i in tweet if i]
                for i in range(len(tweet)-1):
                    phrase=tweet[i]+' '+tweet[i+1]
                    if word in biModel:
                        ind=biModel.index(phrase)
                        biVector[ind]=1
                vector=vector+biVector

                triVector=[0]*len(triModel)
                tweet=[i.strip(specialChar).lower() for i in tweet]
                tweet=[i for i in tweet if i]
                for i in range(len(tweet)-2):
                    phrase=tweet[i]+' '+tweet[i+1]+' '+tweet[i+2]
                    if word in triModel:
                        ind=triModel.index(phrase)
                        triVector[ind]=1
                vector=vector+triVector

#                print vector
                featureVectorsTrain.append(vector)
    f.close()
    print "Feature Vectors Train Created....."
    
    """for each new tweet create a feature vector and feed it to above model to get label"""
    
    testingLabel=[]
    data=[]
    data1=[]
    f=open(sys.argv[2],'r')
    featureVectorsTest=[]
    for i in f:
        if i:
            i=i.split('\t')
            tweet=i[1].split()
            token=i[2].split()
            label=i[3].strip()
            if tweet:
                data.append(label)
                testingLabel.append(encode[label])
                vector=[]
                vector,polarityDictionary=findFeatures(tweet, token, polarityDictionary, stopWords, emoticonsDict, acronymDict)

                uniVector=[0]*len(uniModel)
                for i in tweet:
                    word=i.strip(specialChar).lower()
                    if word:
                        if word in uniModel:
                            ind=uniModel.index(word)
                            uniVector[ind]=1
                vector=vector+uniVector

                biVector=[0]*len(biModel)
                tweet=[i.strip(specialChar).lower() for i in tweet]
                tweet=[i for i in tweet if i]
                for i in range(len(tweet)-1):
                    phrase=tweet[i]+' '+tweet[i+1]
                    if word in biModel:
                        ind=biModel.index(phrase)
                        biVector[ind]=1
                vector=vector+biVector

                triVector=[0]*len(triModel)
                tweet=[i.strip(specialChar).lower() for i in tweet]
                tweet=[i for i in tweet if i]

                for i in range(len(tweet)-2):
                    phrase=tweet[i]+' '+tweet[i+1]+' '+tweet[i+2]
                    if word in triModel:
                        ind=triModel.index(phrase)
                        triVector[ind]=1
                vector=vector+triVector
                featureVectorsTest.append(vector)
    f.close()
    print "Feature Vectors of test input created. Calculating Accuracy..."

    predictedLabel = svmClassifier(trainingLabel,testingLabel,featureVectorsTrain,featureVectorsTest)

    for i in range(len(predictedLabel)):
        givenLabel = predictedLabel[i]
        label = encode.keys()[encode.values().index(givenLabel)]
        data1.append(label)

    f=open('./code/taskB.gs','w')
    f.write('\n'.join(data))
    f.close()

    f=open('./code/taskB.pred','w')
    f.write('\n'.join(data1))
    f.close()
    
    #print len(featureVectorsTest)
    #print len(testingLabel)
    #print len(featureVectorsTrain)
    #print len(trainingLabel)

    #svmClassifier(trainingLabel,testingLabel,featureVectorsTrain,featureVectorsTest)
    #naiveBayesClassifier(trainingLabel,testingLabel,featureVectorsTrain,featureVectorsTest)
