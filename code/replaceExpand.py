def removeStopWords(tweet, token, stopWordsDict):    
    ''' removes stop words in the tweet from the given stop word list'''
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











