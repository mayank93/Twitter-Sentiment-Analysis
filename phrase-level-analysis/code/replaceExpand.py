import re

positive=0
negative=1
neutral=2
total=3
specialChar='1234567890#@%^&()_=`{}:"|[]\;\',./\n\t\r '
listSpecialTag = ['#','U','@',',','E','~','$','G']

def replaceHashtag(tweet, token):
    """takes as input a list which contains words in tweet and return list of words in tweet after replacement 
    #*** - > # """
    for i in range(len(tweet)):
        if token[i]=='#' or tweet[i].startswith('#'):
            token[i]='#'
            tweet[i]=tweet[i][1:].strip(specialChar)
    return tweet,token


def removeNonEnglishWords(tweet,token):
    """remove the non-english or better non-ascii characters
    takes as input a list of words in tweet and a list of corresponding tokens, 
    not using tokens now but may use in future
    and return the modified list of token and words"""

    newTweet=[]
    newToken=[]
    for i in range(len(tweet)):
        if tweet[i]!='':
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
        if stopWordsDict[tweet[i].lower().strip(specialChar)] == 0:
            newTweet.append(tweet[i])
            newToken.append(token[i])
    return newTweet, newToken


def replaceEmoticons(emoticonsDict,tweet,token):
    """replaces the emoticons present in tweet with its polarity
    takes as input a emoticons dict which has emoticons as key and polarity as value
    and a list which contains words in tweet and return list of words in tweet after replacement"""
    
    for i in range(len(tweet)):
        if tweet[i] in emoticonsDict:
            tweet[i]=emoticonsDict[tweet[i]]
            token[i]='E'
    return tweet,token


def expandAcronym(acronymDict,tweet,token):
    """expand the Acronym present in tweet 
    takes as input a acronym dict which has acronym as key and abbreviation as value,
    a list which contains words in tweet and a list of token and return list of words in tweet after expansion and tokens"""
    newTweet=[]
    newToken=[]
    count=0
    for i in range(len(tweet)):
        word=tweet[i].lower().strip(specialChar)
        if word:
            if word in acronymDict:
                count+=1
                newTweet+=acronymDict[word][0]
                newToken+=acronymDict[word][1]

            else:
                newTweet+=[tweet[i]]
                newToken+=[token[i]]
    return newTweet, newToken,count


def replaceRepetition(tweet):
    """takes as input a list which contains words in tweet and return list of words in tweet after replacement and numner of repetion
       eg coooooooool -> coool """
    count=0
    for i in range(len(tweet)):
        x=list(tweet[i])
        if len(x)>3:
            flag=0
            for j in range(3,len(x)):
                if(x[j-3].lower()==x[j-2].lower()==x[j-1].lower()==x[j].lower()):
                    x[j-3]=''

                    if flag==0:
                        count+=1
                        flag=1
            tweet[i]=''.join(x).strip(specialChar)

    return tweet,count


def replaceNegation(tweet):
    """takes as input a list which contains words in tweet and return list of words in tweet after replacement of "not","no","n't","~"
       eg isn't -> negation 
       not -> negation """   
    for i in range(len(tweet)):
        word=tweet[i].lower().strip(specialChar)
        if(word=="no" or word=="not" or word.count("n't")>0):
            tweet[i]='negation'

    return tweet


def expandNegation(tweet,token):
    """takes as input a list which contains words in tweet and return list of words in tweet after expanding of "n't" to "not"
       eg isn't -> is not """
    
    newTweet=[]
    newToken=[]
    for i in range(len(tweet)):
        word=tweet[i].lower().strip(specialChar)
        if(word[-3:]=="n't"):
            if word[-5:]=="can't" :
                newTweet.append('can')
            else:
                newTweet.append(word[:-3])
            newTweet.append('not')
            newToken.append('V')
            newToken.append('R')
        else:
            newTweet.append(tweet[i])
            newToken.append(token[i])
    return newTweet,newToken


def removeTarget(tweet, token):
    """takes as input a list which contains words in tweet and return list of words in tweet after replacement 
    @**** -> @ """
    newToken=[]
    newTweet=[]
    for i in range(len(tweet)):
        if token[i]=='@' or tweet[i].startswith('@'):
            continue
        else:
            newTweet.append(tweet[i])
            newToken.append(token[i])
    return newTweet, newToken


def removeUrl(tweet, token):
    """takes as input a list which contains words in tweet and return list of words in tweet after replacement 
    www.*.* ->'URL' """
    newToken=[]
    newTweet=[]
    for i in range(len(tweet)):
        if token[i]!='U':
            newTweet.append(tweet[i])
            newToken.append(token[i])
    return newTweet, newToken

def removeNumbers(tweet, token):
    """takes as input a list which contains words in tweet and return list of words in tweet after removing 
    numbers """
    newToken=[]
    newTweet=[]
    for i in range(len(tweet)):
        if token[i]!='$':
            newTweet.append(tweet[i])
            newToken.append(token[i])
    return newTweet, newToken

def removeProperCommonNoun(tweet, token):
    """takes as input a list which contains words in tweet and return list of words in tweet after removing 
    numbers """
    newToken=[]
    newTweet=[]
    for i in range(len(tweet)):
        if token[i]!='^' and token[i]!='Z' and token[i]!='O':
            newTweet.append(tweet[i])
            newToken.append(token[i])
    return newTweet, newToken

def removePreposition(tweet, token):
    """takes as input a list which contains words in tweet and return list of words in tweet after removing 
    numbers """
    newToken=[]
    newTweet=[]
    for i in range(len(tweet)):
        if token[i]!='P':
            newTweet.append(tweet[i])
            newToken.append(token[i])
    return newTweet, newToken

def preprocesingTweet1(tweet, token, emoticonsDict, acronymDict):
    """preprocess the tweet """
    tweet,token = replaceEmoticons(emoticonsDict,tweet,token)
    tweet, token = removeNonEnglishWords(tweet, token)
    tweet, token = removeNumbers(tweet, token)
    tweet, token = removeProperCommonNoun(tweet, token)
    tweet, token = removePreposition(tweet, token)
    tweet, token, count1 = expandAcronym(acronymDict,tweet,token)
    tweet, count2 = replaceRepetition(tweet)
    tweet,token = replaceHashtag (tweet, token)
    tweet,token = removeUrl(tweet, token)
    tweet, token = removeTarget(tweet, token)
    tweet,token = expandNegation (tweet, token)
    return tweet, token, count1, count2


def preprocesingTweet2(tweet, token, stopWords):
    """preprocess the tweet """
    tweet = replaceNegation(tweet)
    tweet, token = removeStopWords(tweet, token, stopWords)
    return tweet, token
