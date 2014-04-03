import os
from settings import *

def tokenize(tweet):
    """takes a tweet and return the tokenized tweet along with confidence in following format
    Tokenization \t POSTags \t Confidences \t OriginalData"""
    cwd=os.getcwd()
    program=os.path.join(appPath+,'modules','ark-tweet-nlp-0.3.2','runTagger.sh')
    inputFile=os.path.join(appPath,'modules','ark-tweet-nlp-0.3.2','input.txt')
    outputFile=os.path.join(appPath+'modules','ark-tweet-nlp-0.3.2','output.txt')
    f=open(inputFile,'w')
    f.write(tweet+'\n')
    f.close()
    command=program+' < '+inputFile+' > '+outputFile
    os.system(command)
    f=open(outputFile,'r')
    data=f.read()
    f.close()
    return data
