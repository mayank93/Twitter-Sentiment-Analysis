def replaceEmoticons(emoticonsDict,tweet):
    """replaces the emoticons present in tweet with its polarity
    takes as input a emoticons dict which has emoticons as key and polarity as value
    and a list which contains words in tweet and return list of words in tweet after replacement"""

    for i in range(len(tweet)):
        if tweet[i] in emoticonsDict:
            tweet[i]=emoticonsDict[tweet[i]]
    return tweet




def replaceUrl(tweet):
    """takes as input a list which contains words in tweet and return list of words in tweet after replacement 
    www.*.* ->'URL' """
    for i in range(len(tweet)):
        pass
    return tweet




def replaceRepetition(tweet):
    """takes as input a list which contains words in tweet and return list of words in tweet after replacement 
       eg coooooooool -> coool """
    for i in range(len(tweet)):
        x=list(tweet[i])
        print x
        if len(x)>3:
            for j in range(3,len(x)):
                if(x[j-3].lower()==x[j-2].lower()==x[j-1].lower()==x[j].lower()):
                    x[j-3]=''
            print x
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




if __name__ == '__main__':
    # write this in main file
    f=open("emoticonsWithPolarity.txt",'r').read().split('\n')
    emoticonsDict={}
    for i in f:
        if i:
            print i
            i=i.split()
            value=i[-1]

            key=i[:-1]
            print key
            for j in key:
                print j
                emoticonsDict[j]=value
    print replaceEmoticons(emoticonsDict,['mayank',':-)','\m/','','hello'])
    print replaceRepetition(['mayank','coooooooool','ooooooooooo','heeeeeeeeeeeeeeeelloooooo'])
    print replaceNegation(['mayank',"is't","isn't",'no','not','ji',"dflkjdgfn't",'NO','nO','No'])




