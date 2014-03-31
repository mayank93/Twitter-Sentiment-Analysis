"""This code extracts the features and returns the features"""
from replaceExpand import *
from featureExtractor import *
from probablityModel import *
import sys
from collections import defaultdict
from svmutil import *
#from sklearn import naive_bayes
#from sklearn.externals import joblib

def svmClassifier(trainingLabel,testingLabel,featureVectorsTrain,featureVectorsTest):
    
    """Feed the feature vector to svm to create model"""
    print "Creating SVM Model"
    model= svm_train(trainingLabel,featureVectorsTrain)
    print "Model created. Saving..."

    """Save model"""
    svm_save_model('sentimentAnalysisSVM.model', model)
    print "Model Saved. Proceed to test..."

    predictedLabel, predictedAcc, predictedValue = svm_predict(testingLabel, featureVectorsTest, model)
    print "Finished. The accuracy is:"
    print predictedAcc[0]

def naiveBayesClassifier(trainingLabel,testingLabel,featureVectorsTrain,featureVectorsTest):
    """Feed the feature vector to svm to create model"""
    print "Creating Naive Bayes Model"
    #mnb = naive_bayes.MultinomialNB() #Does not work as features can be negative
    mnb = naive_bayes.GaussianNB()
    mnb.fit(featureVectorsTrain,trainingLabel)
    print "Model created. Saving..."

    """Save model"""
    joblib.dump(mnb, 'sentimentAnalysisNaiveBayes.pkl', compress=9)
    ## To load
    #model_clone = joblib.load('sentimentAnalysisNaiveBayes.pkl')
    print mnb.score(featureVectorsTest,testingLabel)

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

    #print emoticonsDict

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
            acronymDict[key]=[value,token]
    f.close()

    #print acronymDict

    """create stopWords dictionary"""
    stopWords=defaultdict(int)
    f=open("stopWords.txt", "r")
    for line in f:
        if line:
            line=line.strip(specialChar).lower()
            stopWords[line]=1
    f.close()

    priorScore=dict(map(lambda (k,v): (frozenset(reduce( lambda x,y:x+y,[[i] if i not in acronymDict else acronymDict[i][0] for i in k.split()])),int(v)),[ line.split('\t') for line in open("AFINN-111.txt") ]))

    #print priorScore

    encode={'positive': 1,'negative': 2,'neutral':3}

    polarityDictionary = {}

    """create Unigram Model"""
    print "Creating Unigram Model......."
    uniModel=[]
    f=open('unigram.txt','r')
    for line in f:
        if line:
            line=line.strip('\r\t\n ')
            uniModel.append(line)
    uniModel.sort()

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
                uniVector=[0]*len(uniModel)
                for i in tweet:
                    word=i.strip(specialChar).lower()
                    if word:
                        if word in uniModel:
                            ind=uniModel.index(word)
                            uniVector[ind]=1
                vector=vector+uniVector
#                print vector
                featureVectorsTrain.append(vector)
    f.close()
    print "Feature Vectors Train Created....."
    
    """for each new tweet create a feature vector and feed it to above model to get label"""
    testingLabel=[]
    f=open(sys.argv[2],'r')
    featureVectorsTest=[]
    for i in f:
        if i:
            i=i.split('\t')
            tweet=i[1].split()
            token=i[2].split()
            label=i[3].strip()
            if tweet:
                testingLabel.append(encode[label])
                vector,polarityDictionary=findFeatures(tweet, token, polarityDictionary, stopWords, emoticonsDict, acronymDict)
                uniVector=[0]*len(uniModel)
                for i in tweet:
                    word=i.strip(specialChar).lower()
                    if word:
                        if word in uniModel:
                            ind=uniModel.index(word)
                            uniVector[ind]=1
                vector=vector+uniVector
                featureVectorsTest.append(vector)
    f.close()
    print "Feature Vectors of test input created. Calculating Accuracy..."

    svmClassifier(trainingLabel,testingLabel,featureVectorsTrain,featureVectorsTest)
    #naiveBayesClassifier(trainingLabel,testingLabel,featureVectorsTrain,featureVectorsTest)
