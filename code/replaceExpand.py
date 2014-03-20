import re

def removeNonEnglishWords(tweet,token):
    """remove the non-english or better non-ascii characters
    takes as input a list of words in tweet and a list of corresponding tokens, 
    not using tokens now but may use in future
    and return the modified list of token and words"""

    newTweet=[]
    newToken=[]
    for i in range(len(tweet)):
        chk=re.match(r'([a-zA-z0-9 \+\?\.\*\^\$\(\)\[\]\{\}\|\\/:;\'\"><,.#@!~`%&-_=])+$',tweet[i])
        if chk:
            newTweet.append(tweet[i])
            newToken.append(token[i])
    return newTweet, newToken




def removeStopWords(tweet, token, stopWordsDict):    
    """remove the stop words ,
    takes as input a list of words in tweet ,a list of corresponding tokens and a stopWords Dictonary, 
    and return the modified list of token and words"""

    newTweet=[]
    newToken=[]
    for i in range(len(tweet)):
        if stopWordsDict[tweet[i]] == 0:
            newTweet.append(tweet[i])
            newToken.append(token[i])
    return newTweet, newToken




def replaceEmoticons(emoticonsDict,tweet):
    """replaces the emoticons present in tweet with its polarity
    takes as input a emoticons dict which has emoticons as key and polarity as value
    and a list which contains words in tweet and return list of words in tweet after replacement"""
    
    for i in range(len(tweet)):
        if tweet[i] in emoticonsDict:
            tweet[i]=emoticonsDict[tweet[i]]
    return tweet




def replaceUrl(tweet, token):
    """takes as input a list which contains words in tweet and return list of words in tweet after replacement 
    www.*.* ->'URL' """
    for i in range(len(tweet)):
        if token[i]=='U':
            tweet[i]='U'
    return tweet




def replaceHashtag(tweet, token):
    """takes as input a list which contains words in tweet and return list of words in tweet after replacement 
    #*** - > # """
    for i in range(len(tweet)):
        if token[i]=='#':
            tweet[i]='#'
    return tweet




def replaceTarget(tweet, token):
    """takes as input a list which contains words in tweet and return list of words in tweet after replacement 
    @**** -> @ """
    for i in range(len(tweet)):
        if token[i]=='@':
            tweet[i]='@'
    return tweet



def replaceRepetition(tweet):
    """takes as input a list which contains words in tweet and return list of words in tweet after replacement 
       eg coooooooool -> coool """
    for i in range(len(tweet)):
        x=list(tweet[i])
        if len(x)>3:
            for j in range(3,len(x)):
                if(x[j-3].lower()==x[j-2].lower()==x[j-1].lower()==x[j].lower()):
                    x[j-3]=''
            tweet[i]=''.join(x)

    return tweet




def replaceNegation(tweet):
    """takes as input a list which contains words in tweet and return list of words in tweet after replacement of "not","no","n't","~"
       eg isn't -> negation 
       not -> negation """
    
   
    for i in range(len(tweet)):
        if(tweet[i].lower()=="no" or tweet[i].lower()=="not" or tweet[i][0].lower()=="~" or tweet[i][-3:].lower()=="n't"):
            tweet[i]='negation'

    return tweet




def preprocesingTweet(tweet, token, stopWords, emoticonsDict,feature):
    """preprocess the tweet """
    tweet, token = removeNonEnglishWords(tweet, token)
    print tweet
    tweet, token = removeStopWords(tweet, token, stopWords)
    tweet = replaceEmoticons(emoticonsDict, tweet)
    tweet = replaceRepetition(tweet)
    tweet = replaceNegation(tweet)
    tweet = replaceUrl (tweet, token)
    tweet = replaceHashtag (tweet, token)
    tweet = replaceTarget (tweet, token)

    return tweet,token
