import re

positive=0
negative=1
neutral=2
total=3
specialChar='1234567890@#%^&()_=`{}:"|[]\;\',./\n\t\r '
listSpecialTag = ['#','U','@',',','E','~','$','G']


def removeNonEnglishWords(tweet,token,start,end):
    """remove the non-english or better non-ascii characters
    takes as input a list of words in tweet and a list of corresponding tokens, 
    not using tokens now but may use in future
    and return the modified list of token and words"""

    newTweet=[]
    newToken=[]
    for i in range(len(tweet)):
        chk=re.match(r'([a-zA-z0-9 \+\?\.\*\^\$\(\)\[\]\{\}\|\\/:;\'\"><,.#@!~`%&-_=])+$',tweet[i])
        if chk:
            newTweet.append(tweet[i].strip(specialChar))
            newToken.append(token[i])
        else:
            start=start-1
            end=end-1
    return newTweet, newToken,start,end




def removeStopWords(tweet, token, stopWordsDict,start,end):    
    """remove the stop words ,
    takes as input a list of words in tweet ,a list of corresponding tokens and a stopWords Dictonary, 
    and return the modified list of token and words"""

    newTweet=[]
    newToken=[]
    for i in range(len(tweet)):
        if stopWordsDict[tweet[i].lower().strip(specialChar)] == 0:
            newTweet.append(tweet[i])
            newToken.append(token[i])
        else:
            start=start-1
            end=end-1
    return newTweet, newToken,start,end




def replaceEmoticons(emoticonsDict,tweet,token):
    """replaces the emoticons present in tweet with its polarity
    takes as input a emoticons dict which has emoticons as key and polarity as value
    and a list which contains words in tweet and return list of words in tweet after replacement"""
  
    for i in range(len(tweet)):
        if tweet[i] in emoticonsDict:
           
            tweet[i]=emoticonsDict[tweet[i]]
            token[i]='E'
        
    return tweet,token




def expandAcronym(acronymDict,tweet,token,start,end):
    """expand the Acronym present in tweet 
    takes as input a acronym dict which has acronym as key and abbreviation as value,
    a list which contains words in tweet and a list of token and return list of words in tweet after expansion and tokens"""
    count=0
    newTweet=[]
    newToken=[]
    for i in range(len(tweet)):
        word=tweet[i].lower().strip(specialChar)
        if 1:
            count+=1
            if word in acronymDict:
                newTweet+=acronymDict[word][0]
                newToken+=acronymDict[word][1]
                start=start+len(acronymDict[word][0])-1
                end=end+len(acronymDict[word][0])-1

            else:
                newTweet+=[tweet[i]]
                newToken+=[token[i]]
            
    return newTweet, newToken, count,start,end




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
        if token[i]=='#' or tweet[i].startswith('#'):
            token[i]='#'
            tweet[i]=tweet[i][:].strip(specialChar)
    return tweet,token




def replaceTarget(tweet, token):
    """takes as input a list which contains words in tweet and return list of words in tweet after replacement 
    @**** -> @ """
    for i in range(len(tweet)):
        if token[i]=='@' or tweet[i].startswith('@'):
            token[i]='@'
            tweet[i]=tweet[i][:].strip(specialChar)
            #tweet[i]=''
    return tweet,token



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



def expandNegation(tweet,token,start,end):
    """takes as input a list which contains words in tweet and return list of words in tweet after expanding of "n't" to "not"
       eg isn't -> is not """
    
    newTweet=[]
    newToken=[]
   
    for i in range(len(tweet)):
        word=tweet[i].lower().strip(specialChar)
        if(word[-3:]=="n't"):
            newTweet.append(word[:-3])
            newTweet.append('not')
            newToken.append('V')
            newToken.append('R')
            start=start+1
            end=end+1
        else:
            newTweet.append(tweet[i])
            newToken.append(token[i])
    return newTweet,newToken,start,end





def preprocesingTweet1(tweet, token,start,end, emoticonsDict, acronymDict,stopWords):
    """preprocess the tweet """

    
    # print "tweet before %s,%d %d %d" %(tweet,len(tweet),start,end)
    tweet, token, count1,start,end = expandAcronym(acronymDict,tweet,token,start,end)
    
    # print "tweet after %s,%d %d %d" %(tweet,len(tweet),start,end)
    tweet,token,start,end = expandNegation (tweet, token,start,end)
    tweet,count2 = replaceRepetition(tweet)
    tweet,token = replaceEmoticons(emoticonsDict, tweet,token)
    tweet = replaceUrl (tweet, token)
    #print "tweet before %s,%d %d %d" %(tweet,len(tweet),start,end) 
    tweet,token = replaceHashtag (tweet, token)
    #print "tweet before %s,%d %d %d" %(tweet,len(tweet),start,end) 
    tweet,token = replaceTarget (tweet, token)
    tweet=replaceNegation(tweet)
    tweet, token,start,end = removeNonEnglishWords(tweet, token,start,end)
    #print "tweet before %s,%d %d %d" %(tweet,len(tweet),start,end)
    #tweet, token,start,end = removeStopWords(tweet, token, stopWords,start,end)
    #print "tweet after %s,%d %d %d" %(tweet,len(tweet),start,end)
    
    return tweet, token,start,end



"""
def preprocesingTweet2(tweet, token,start,end, stopWords):
   
    tweet = replaceNegation(tweet)
   # tweet, token = removeStopWords(tweet, token, stopWords)
#    print tweet

    return tweet, token,start,end
"""
