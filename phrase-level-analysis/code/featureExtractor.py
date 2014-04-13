from senti_classifier import senti_classifier
from replaceExpand import *
from nltk.corpus import wordnet

#syns = wordnet.synsets('car')
#synonyms = [l.name for s in syns for l in s.lemmas]

def calculateScore(tweet, polarityDictionary):
    score = {}
    tweet=[i.lower().strip(specialChar) for i in tweet]
    tweet=[i for i in tweet if i]
    length=len(tweet)
    init=0
    neutralScore=0
    while init<length:
        for i in range(init,length):
            flag=0
            for j in range(length,i,-1):
                phrase=frozenset(tweet[i:j])
                if phrase in polarityDictionary:
                    init=j
                    flag=1
                    posScore = polarityDictionary[phrase][positive]
                    negScore = polarityDictionary[phrase][negative]
                    neutralScore = polarityDictionary[phrase][neutral]
                    score[phrase]=[posScore, negScore, neutralScore]
                    break
            if flag==1:
                break
            else:
                posScore, negScore = senti_classifier.polarity_scores([tweet[i]])
                score[frozenset([tweet[i]])]=[posScore, negScore, neutralScore]
                polarityDictionary[frozenset([tweet[i]])]=[posScore, negScore, neutralScore]
    return score,polarityDictionary




def findCapitalised(tweet, token, score):
    count=0
    countCap = 0
    countCapPos = 0
    countCapNeg = 0
    isCapitalised = 0
    for i in range(len(tweet)):
        if token[i]!='$':
            word=tweet[i].strip(specialChar)
            if word:
                count+=1
                if word.isupper():
                    countCap += 1
                    word=frozenset([word.lower()])
                    for phrase in score.keys():
                        if word.issubset(phrase):
                                if score[phrase][positive]!=0.0:
                                    countCapPos +=1
                                if score[phrase][negative]!=0.0:
                                    countCapNeg +=1
    percentageCapitalised = 0.0
    if count>0:
        percentageCapitalised = float(countCap)/count
    if percentageCapitalised!=0.0:
	    isCapitalised=1
    return [ percentageCapitalised, countCapPos, countCapNeg ,isCapitalised ]
#    return [ percentageCapitalised, isCapitalised ]




def findNegation(tweet):
	countNegation = 0
	for i in range(len(tweet)):
		if tweet[i]=='negation':
			countNegation+=1
	return [countNegation]




def findTotalScore(score):
    totalScore = 0
    for i in score.values():
        totalScore += (i[positive] - i[negative])
    return [ totalScore ]




def findPositiveNegativeWords(tweet, token, score):
    countPos=0
    countNeg=0
    count=0
    totalScore = 0
    if tweet:
        for i in range(len(tweet)):
            if token[i] not in listSpecialTag:
                word=frozenset([tweet[i].lower().strip(specialChar)])
                if word:
                    count+=1
                    for phrase in score.keys():
                        if word.issubset(phrase):
                            if score[phrase][positive]!=0.0:
	                            countPos+=1
                            if score[phrase][negative]!=0.0:
                                countNeg+=1
                            totalScore += (score[phrase][positive] - score[phrase][negative])
    return [ countPos, countNeg, totalScore ]
#	return [ count ]
	



def findEmoticons(tweet, token):
	countEmoPos = 0
	countEmoNeg =0
	countEmoExtremePos = 0
	countEmoExtremeENeg = 0

	for i in range(len(tweet)):
	    if token[i] ==  'E':
			if tweet[i] == 'Extremely-Positive':
				countEmoExtremePos+=1
			if tweet[i] == 'Extremely-Negative':
				countEmoExtremeENeg+=1
			if tweet[i] == 'Positive':
				countEmoPos+=1
			if tweet[i] == 'Negative':
				countEmoNeg+=1

	return [ countEmoPos, countEmoNeg, countEmoExtremePos, countEmoExtremeENeg ]




def findHashtag( tweet, token, score):
	
    countHashPos=0
    countHashNeg=0
    count=0
    for i in range(len(tweet)):
        if token[i]=='#' :
            count+=1
            word=frozenset([tweet[i].lower().strip(specialChar)])
            if word:
                for phrase in score.keys():
                    if word.issubset(phrase):
                        if score[phrase][positive]!=0.0:
                            countHashPos+=1
                        if score[phrase][negative]!=0.0:
                            countHashNeg+=1
                        break
    return [ countHashPos, countHashNeg ]
#    return [ count ]




def countSpecialChar(tweet,score):
    count={'?':0,'!':0,'*':0}
#    count={'?':[0,0],'!':[0,0],'*':[0,0]}
    for i in range(len(tweet)):
        word=tweet[i].lower().strip(specialChar)
#        word=frozenset([tweet[i].lower().strip(specialChar)])
        if word:
            count['?']+=word.count('?')
            count['!']+=word.count('!')
            count['*']+=word.count('*')
            """
            for phrase in score.keys():
                if word.issubset(phrase):
                    word=''.join(list(word))
                    if score[phrase][positive]!=0.0:
                        count['?'][positive]+=word.count('?')
                        count['!'][positive]+=word.count('!')
                        count['*'][positive]+=word.count('*')
                    if score[phrase][negative]!=0.0:
                        count['?'][negative]+=word.count('?')
                        count['!'][negative]+=word.count('!')
                        count['*'][negative]+=word.count('*')
                    break
            """
    return [ count['?'], count['!'], count['*'] ]
#    return [ count['?'][positive], count['!'][positive], count['*'][positive], count['?'][negative], count['!'][negative], count['*'][negative] ]




def countPosTag(tweet,token,score):
    count={'N':0,'V':0,'R':0,'P':0,'O':0,'A':0}
#    count={'N':[0,0],'V':[0,0],'R':[0,0],'P':[0,0],'O':[0,0],'A':[0,0]}
    for i in range(len(tweet)):
        word=tweet[i].lower().strip(specialChar)
#        word=frozenset([tweet[i].lower().strip(specialChar)])
        if word:
            if token[i] in count:
                count[token[i]]+=1
            """           
            for phrase in score.keys():
                if word.issubset(phrase):
                    word=''.join(list(word))
                    if score[phrase][positive]!=0.0:
                        if token[i] in count:
                            count[token[i]][positive]+=1
                    if score[phrase][negative]!=0.0:
                        if token[i] in count:
                            count[token[i]][negative]+=1
                    break
            """

    return [ count['N'], count['V'], count['R'], count['P'], count['O'], count['A'] ]
#    return [ count['N'][positive], count['V'][positive], count['R'][positive], count['P'][positive], count['O'][positive], count['A'][positive], count['N'][negative], count['V'][negative], count['R'][negative], count['P'][negative], count['O'][negative], count['A'][negative] ]

def findUrl(tweet,token):
    count = 0
    for i in range(len(tweet)):
        if token[i] ==  'U':
            count+=1
    return [count]



def findFeatures(tweet, token, polarityDictionary, stopWords, emoticonsDict, acronymDict):
    """takes as input the tweet and token and returns the feature vector"""

    tweet,token,count1,count2 = preprocesingTweet1(tweet, token, emoticonsDict, acronymDict) 
    score,polarityDictionary = calculateScore(tweet, polarityDictionary)
    featureVector=[]
    featureVector.extend(findTotalScore(score))
    tweet,token=preprocesingTweet2(tweet, token, stopWords)
    featureVector.extend(findCapitalised( tweet, token, score))
    featureVector.extend(findHashtag( tweet, token, score))
    featureVector.extend(findEmoticons(tweet, token))
    featureVector.extend(findNegation(tweet))
    featureVector.extend(findPositiveNegativeWords(tweet,token, score))
   # #featureVector.extend(findUrl(tweet,token))
#   # featureVector.extend([count1])  # number of acronym
#    #featureVector.extend([count2])  # number of words which had repetion
    featureVector.extend(countSpecialChar(tweet,score))  # number of  special char
    featureVector.extend(countPosTag(tweet,token,score))
    return featureVector, polarityDictionary
