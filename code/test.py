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

    """Load Model"""
	model= svm_load_model('sentimentAnalysis.model')

	"""Load Polarity Dictionary"""


	f=open('./ark-tweet-nlp-0.3.2/tweetTokenised.txt','r')
    featureVectors=[]
    for i in f:
        if i:
            i=i.split('\t')
            tweet=i[1].split()
            token=i[2].split()
            tweet,token=preprocesingTweet(tweet, token, stopWords, emoticonsDict, acronymDict)
            if tweet:
                featureVectors=findFeatures(tweet, token, polarityDictionary)
                predictedLabel, predictedAcc, predictedValue = svm_predict([1], featureVectors, model, '-b 1')
                print predictedLabel
    
