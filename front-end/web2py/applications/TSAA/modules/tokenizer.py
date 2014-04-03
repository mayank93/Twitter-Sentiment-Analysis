import os
import random
from settings import *

def tokenize(tweet):
    """takes a tweet and return the tokenized tweet along with confidence in following format
    Tokenization \t POSTags \t Confidences \t OriginalData"""
    cwd=os.getcwd()
    print "hello"
    program=os.path.join(appPath,'modules','ark-tweet-nlp-0.3.2','runTagger.sh')
    inputFile=os.path.join(appPath,'modules','ark-tweet-nlp-0.3.2','tokenized',''.join([ chr(random.randint(97,122)) for i in range(0,20) ]))
    outputFile=os.path.join(appPath,'modules','ark-tweet-nlp-0.3.2','tokenized',''.join([ chr(random.randint(97,122)) for i in range(0,20) ]))
    f=open(inputFile,'w')
    f.write(tweet+'\n')
    f.close()
    command=program+' < '+inputFile+' > '+outputFile
    os.system(command)
    f=open(outputFile,'r')
    data=f.read()
    f.close()
    return data
