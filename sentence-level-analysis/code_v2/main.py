"""This code extracts the features and returns the features"""
from featureExtractor import *
from probablityModel import *
import sys
from classifier import *
from prepare import *
if __name__ == '__main__':
    
    """check arguments"""
    if len(sys.argv)!= 3:                                                   
        print "Usage :: python main.py ../dataset/finalTrainingInput.txt ../dataset/finalTestingInput"
        sys.exit(0)

    acronymDict,stopWords,emoticonsDict = loadDictionary()

    priorScore=dict(map(lambda (k,v): (frozenset(reduce( lambda x,y:x+y,[[i] if i not in acronymDict else acronymDict[i][0] for i in k.split()])),int(v)),[ line.split('\t') for line in open("AFINN-111.txt") ]))

    
    """create Unigram Model"""
    print "Creating Unigram Model......."
    polarityDictionary = probTraining(priorScore)
    print "Unigram Model Created"


    """ polarity dictionary combines prior score """
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
                trainingLabel.append(encode[label])
                vector,polarityDictionary=findFeatures(tweet, token, polarityDictionary, stopWords, emoticonsDict, acronymDict)
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
            data.append(label)
            if tweet:
                testingLabel.append(encode[label])
                vector,polarityDictionary=findFeatures(tweet, token, polarityDictionary, stopWords, emoticonsDict, acronymDict)
                featureVectorsTest.append(vector)
    f.close()
    print "Feature Vectors of test input created. Calculating Accuracy..."

    predictedLabel = svmClassifier(trainingLabel,testingLabel,featureVectorsTrain,featureVectorsTest)

    for i in range(len(predictedLabel)):
        givenLabel = predictedLabel[i]
        label = encode.keys()[encode.values().index(givenLabel)]
        data1.append(label)

    f=open('taskB.gs','w')
    f.write('\n'.join(data))
    f.close()

    f=open('taskB.pred','w')
    f.write('\n'.join(data1))
    f.close()

    naiveBayesClassifier(trainingLabel,testingLabel,featureVectorsTrain,featureVectorsTest)