#when u want to train the model again run this


from settings import *
from collections import defaultdict
from SentenceLevel import featureExtractor as sentenceFeatureExtractor, probablityModel as sentenceProbablityModel, classifier as sentenceClassifier, prepare as sentencePrepare , replaceExpand as sentenceReplaceExpand
from PhraseLevel import featureExtractor as phraseFeatureExtractor, probablityModel as phraseProbablityModel, classifier as phraseClassifier, prepare as phrasePrepare , replaceExpand as phraseReplaceExpand
import time

while True:

	""" sentence level model """
   	rows = db(db.SentTrainDetails.id>0).select()
    	#print rows
    	trainFile=os.path.join(appPath,'modules','SentenceLevel','trainData.txt')
    	f=open(trainFile,'w')
    	"""get unique tweets and make uni,bi,tri gram model """
    	"""for each row extract the tweet,token,label and do preprocesing and create a feature vector"""
    	for row in rows:
	    	f.write(str(row.id)+'\t'+str(row.Tweet)+'\t'+str(row.Token)+'\t'+str(row.Label)+'\n')
    	f.close()

    	emoticonsFile=os.path.join(appPath,'modules','SentenceLevel','emoticonsWithPolarity.txt')
    	acronymFile=os.path.join(appPath,'modules','SentenceLevel','acronym_tokenised.txt')
    	stopWordsFile=os.path.join(appPath,'modules','SentenceLevel','stopWords.txt')
    
    	unigramProgram=os.path.join(appPath,'modules','SentenceLevel','unigramFilter.py')
    	uniFile=os.path.join(appPath,'modules','SentenceLevel','unigram.txt')
    	command='python '+unigramProgram+' '+emoticonsFile+' '+acronymFile+' '+stopWordsFile+' '+trainFile+' > '+uniFile
    	os.system(command)
    
    	bigramProgram=os.path.join(appPath,'modules','SentenceLevel','bigramFilter.py')
    	biFile=os.path.join(appPath,'modules','SentenceLevel','bigram.txt')
    	command='python '+bigramProgram+' '+emoticonsFile+' '+acronymFile+' '+stopWordsFile+' '+trainFile+' > '+biFile
    	os.system(command)
	
	trigramProgram=os.path.join(appPath,'modules','SentenceLevel','trigramFilter.py')
	triFile=os.path.join(appPath,'modules','SentenceLevel','trigram.txt')
	command='python '+trigramProgram+' '+emoticonsFile+' '+acronymFile+' '+stopWordsFile+' '+trainFile+' > '+triFile
	os.system(command)

	
	acronymDict,stopWords,emoticonsDict = sentencePrepare.loadDictionary(emoticonsFile, acronymFile, stopWordsFile)

	affinFile=os.path.join(appPath,'modules','SentenceLevel','AFINN-111.txt')
    	priorScore=dict(map(lambda (k,v): (frozenset(reduce( lambda x,y:x+y,[[i] if i not in acronymDict else acronymDict[i][0] for i in k.split()])),int(v)),[ line.split('\t') for line in open(affinFile,'r') ]))
	"""create Unigram Model"""
    	print "Creating Unigram Model......."
    	uniModel=[]
    	f=open(uniFile,'r')
    	for line in f:
    	    if line:
    	        line=line.strip('\r\t\n ')
    	        uniModel.append(line)
    	uniModel.sort()

    	print "Unigram Model Created"

    	print "Creating Bigram Model......."
    	biModel=[]
    	f=open(biFile,'r')
    	for line in f:
    	    if line:
    	        line=line.strip('\r\t\n ')
    	        biModel.append(line)
    	biModel.sort()
    	print "Bigram Model Created"
	
    	print "Creating Trigram Model......."
    	triModel=[]
    	f=open(triFile,'r')
    	for line in f:
    	    if line:
    	        line=line.strip('\r\t\n ')
    	        triModel.append(line)
    	triModel.sort()
    	print "Trigram Model Created"
    	""" polarity dictionary combines prior score """
    	polarityDictionary = sentenceProbablityModel.probTraining(priorScore)
    
    	"""Create a feature vector of training set """
    	print "Creating Feature Vectors....."

    	encode={'positive': 1.0,'negative': 2.0,'neutral':3.0}
    	trainingLabel=[]
    	f=open(trainFile,'r')
    	featureVectorsTrain=[]
    	for i in f:
        	if i:
		    print "hello"
        	    i=i.split('\t')
        	    tweet=i[1].split()
        	    token=i[2].split()
        	    label=i[3].strip()
        	    if tweet:
        	        vector=[]
        	        trainingLabel.append(encode[label])
        	        vector,polarityDictionary=sentenceFeatureExtractor.findFeatures(tweet, token, polarityDictionary, stopWords, emoticonsDict, acronymDict)
        	        uniVector=[0]*len(uniModel)
        	        for i in tweet:
        	            word=i.strip(sentenceReplaceExpand.specialChar).lower()
        	            if word:
        	                if word in uniModel:
        	                    ind=uniModel.index(word)
        	                    uniVector[ind]=1
        	        vector=vector+uniVector
	
                	biVector=[0]*len(biModel)
                	tweet=[i.strip(sentenceReplaceExpand.specialChar).lower() for i in tweet]
                	tweet=[i for i in tweet if i]
                	for i in range(len(tweet)-1):
                	    phrase=tweet[i]+' '+tweet[i+1]
                	    if word in biModel:
                	        ind=biModel.index(phrase)
                	        biVector[ind]=1
                	vector=vector+biVector
	
	                triVector=[0]*len(triModel)
	                tweet=[i.strip(sentenceReplaceExpand.specialChar).lower() for i in tweet]
	                tweet=[i for i in tweet if i]
	                for i in range(len(tweet)-2):
	                    phrase=tweet[i]+' '+tweet[i+1]+' '+tweet[i+2]
	                    if word in triModel:
	                        ind=triModel.index(phrase)
	                        triVector[ind]=1
	                vector=vector+triVector
	
	                #print vector
	                featureVectorsTrain.append(vector)
    	f.close()
    	print "Feature Vectors Train Created....."
	print trainingLabel
	modelPath=os.path.join(appPath,'modules','SentenceLevel','sentimentAnalysisSVM.model')
	"""feed feature vector to svm to get model save it"""
	sentenceClassifier.svmClassifierModel(trainingLabel, featureVectorsTrain, modelPath)
	
	
	
	""" phrase level model """
	"""get unique tweets and make uni,bi,tri gram model """
	rows = db(db.PhraseTrainDetails.id>0).select()
	print rows
    	trainFile=os.path.join(appPath,'modules','PhraseLevel','trainData.txt')
    	f=open(trainFile,'w')
    	"""get unique tweets and make uni,bi,tri gram model """
    	"""for each row extract the tweet,token,label and do preprocesing and create a feature vector"""

    	for row in rows:
	    	f.write(str(row.id)+'\t'+str(row.Tweet)+'\t'+str(row.Token)+'\t'+str(row.Phrase)+'\t'+str(row.Label)+'\n')
    	f.close()

    	emoticonsFile=os.path.join(appPath,'modules','PhraseLevel','emoticonsWithPolarity.txt')
    	acronymFile=os.path.join(appPath,'modules','PhraseLevel','acronym_tokenised.txt')
    	stopWordsFile=os.path.join(appPath,'modules','PhraseLevel','stopWords.txt')
    
    	unigramProgram=os.path.join(appPath,'modules','PhraseLevel','unigramFilter.py')
    	uniFile=os.path.join(appPath,'modules','PhraseLevel','unigram.txt')
    	command='python '+unigramProgram+' '+emoticonsFile+' '+acronymFile+' '+stopWordsFile+' '+trainFile+' > '+uniFile
    	os.system(command)
    
    	bigramProgram=os.path.join(appPath,'modules','PhraseLevel','bigramFilter.py')
    	biFile=os.path.join(appPath,'modules','PhraseLevel','bigram.txt')
    	command='python '+bigramProgram+' '+emoticonsFile+' '+acronymFile+' '+stopWordsFile+' '+trainFile+' > '+biFile
    	os.system(command)
	
	trigramProgram=os.path.join(appPath,'modules','PhraseLevel','trigramFilter.py')
	triFile=os.path.join(appPath,'modules','PhraseLevel','trigram.txt')
	command='python '+trigramProgram+' '+emoticonsFile+' '+acronymFile+' '+stopWordsFile+' '+trainFile+' > '+triFile
	os.system(command)

	
	acronymDict,stopWords,emoticonsDict = phrasePrepare.loadDictionary(emoticonsFile, acronymFile, stopWordsFile)

	affinFile=os.path.join(appPath,'modules','PhraseLevel','AFINN-111.txt')
    	priorScore=dict(map(lambda (k,v): (frozenset(reduce( lambda x,y:x+y,[[i] if i not in acronymDict else acronymDict[i][0] for i in k.split()])),int(v)),[ line.split('\t') for line in open(affinFile,'r') ]))

    
	"""create Unigram Model"""
    	print "Creating Unigram Model......."
    	uniModel=[]
    	f=open(uniFile,'r')
    	for line in f:
    	    if line:
    	        line=line.strip('\r\t\n ')
    	        uniModel.append(line)
    	uniModel.sort()

    	print "Unigram Model Created"

    	print "Creating Bigram Model......."
    	biModel=[]
    	f=open(biFile,'r')
    	for line in f:
    	    if line:
    	        line=line.strip('\r\t\n ')
    	        biModel.append(line)
    	biModel.sort()
    	print "Bigram Model Created"
	
    	print "Creating Trigram Model......."
    	triModel=[]
    	f=open(triFile,'r')
    	for line in f:
    	    if line:
    	        line=line.strip('\r\t\n ')
    	        triModel.append(line)
    	triModel.sort()
    	print "Trigram Model Created"
    	
    	""" polarity dictionary combines prior score """
    	polarityDictionary = phraseProbablityModel.probTraining(priorScore)
		
    
    	"""Create a feature vector of training set """
    	print "Creating Feature Vectors....."

	
    	encode={'positive': 1.0,'negative': 2.0,'neutral':3.0}
    	trainingLabel=[]
    	f=open(trainFile,'r')
    	featureVectorsTrain=[]
    	for i in f:
        	if i:
        	    i=i.split('\t')
        	    tweet=i[1]
            	    token=i[2].split()
		    phrase=i[3].split()
        	    label=i[4].strip()
	    	    tweet=phrase

        	    if tweet:
        	        vector=[]
        	        trainingLabel.append(encode[label])
        	        vector,polarityDictionary=phraseFeatureExtractor.findFeatures(tweet, token, polarityDictionary, stopWords, emoticonsDict, acronymDict)
        	        uniVector=[0]*len(uniModel)
        	        for i in tweet:
        	            word=i.strip(phraseReplaceExpand.specialChar).lower()
        	            if word:
        	                if word in uniModel:
        	                    ind=uniModel.index(word)
        	                    uniVector[ind]=1
        	        vector=vector+uniVector
	
                	biVector=[0]*len(biModel)
                	tweet=[i.strip(phraseReplaceExpand.specialChar).lower() for i in tweet]
                	tweet=[i for i in tweet if i]
                	for i in range(len(tweet)-1):
                	    phrase=tweet[i]+' '+tweet[i+1]
                	    if word in biModel:
                	        ind=biModel.index(phrase)
                	        biVector[ind]=1
                	vector=vector+biVector
	
	                triVector=[0]*len(triModel)
	                tweet=[i.strip(phraseReplaceExpand.specialChar).lower() for i in tweet]
	                tweet=[i for i in tweet if i]
	                for i in range(len(tweet)-2):
	                    phrase=tweet[i]+' '+tweet[i+1]+' '+tweet[i+2]
	                    if word in triModel:
	                        ind=triModel.index(phrase)
	                        triVector[ind]=1
	                vector=vector+triVector
	
	                #print vector
	                featureVectorsTrain.append(vector)
    	f.close()
    	print "Feature Vectors Train Created....."
	print trainingLabel
	modelPath=os.path.join(appPath,'modules','PhraseLevel','sentimentAnalysisSVM.model')    

	"""feed feature vector to svm to get model save it"""
	phraseClassifier.svmClassifierModel(trainingLabel, featureVectorsTrain, modelPath)
	time.sleep(86400)
