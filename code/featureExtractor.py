from senti_classifier import senti_classifier

positive=0
negative=1
neutral = 2

listSpecialTag = ['#','U','@',',','E','~','$','G']

def calculateScore(tweet, polarityDictionary):
	score = {}
	for i in range(len(tweet)):
		if token[i]== '#':
			tweet[i] = tweet[i][1:]
		pos_score, neg_score = senti_classifier.polarity_scores(list(tweet[i]))		
		if tweet[i] in polarityDictionary:
			pos_score += polarityDictionary[tweet][positive]
			neg_score += polarityDictionary[tweet][negative]
			neutral_score = polarityDictionary[tweet][neutral]
			score[tweet[i]]=[pos_score, neg_score, neutral_score]
	return score

def findCapitalised(tweet, score,token):

	countCap = 0
	countCapPos = 0
	countCapNeg = 0
	isCapitalised = 0
	for i in range(len(tweet)):
		if token[i]!='$'
			if tweet[i].isupper():
				countCap += 1
				if score[tweet[i]][0]!=0.0:
					countCapPos +=1
				if score[tweet[i]][1]!=0.0:
					countCapNeg +=1
	percentageCapitalised = float(count)/len(tweet)
	if percentageCapitalised!=0.0:
		isCapitalised=1
	return [ percentageCapitalised, countCapPos, countCapNeg ,isCapitalised]

def findNegation(tweet):
	countNegation = 0
	for i in range(len(tweet)):
		if tweet[i]=='negation':
			countNegation+=1
	return countNegation

def findPositiveNegativeWords(tweet, token, score):
	countPos=0
	countNeg=0
	totalScore = 0
	if token[i] not in listSpecialTag:
		if score[tweet[i]][0]!=0.0:
			countPos+=1
		if score[tweet[i]][1]!=0.0:
			countNeg+=1
	totalScore += (pos_score - neg_score)
	return [countPos, countNeg, totalScore]
	

def findEmoticons(tweet, token):
	countEmoPos = 0
	countEmoNeg =0
	countEmoExtremePos = 0
	countEmoExtremeENeg = 0

	if token[i] ==  'E':
			if tweet[i] == 'Extremely-Positive':
				countEmoExtremePos+=1
			if tweet[i] == 'Extremely-Negative':
				countEmoExtremeENeg+=1
			if tweet[i] == 'Positive':
				countEmoPos+=1
			if tweet[i] == 'Negative':
				countEmoNeg+=1

	return [countEmoPos, countEmoNeg, countEmoExtremePos, countEmoExtremeENeg]

def findHashtag( tweet, token, score):
	
	countHashPos=0
	countHashNeg=0

	if token[i]=='#' :
		if score[tweet[i][1:]][0]!=0.0:
			countHashPos+=1
		if score[tweet[i][1:]][1]!=0.0:
			countHashNeg+=1

	return [countHashPos, countHashNeg]
		

		

def findFeatures(tweet, token, polarityDictionary):
	"""takes as input the tweet and token and returns the feature vector"""

	score =calculateScore(tweet, polarityDictionary)
	featureVector=[]
	featureVector.extend(findCapitalised( tweet, token, score))
	featureVector.extend(findHashtag( tweet, token, score))
	featureVector.extend(findEmoticons(tweet, token))
	featureVector.extend(findNegation(tweet))
	featureVector.extend(findPositiveNegativeWords(tweet,token, score))

	return featureVector
