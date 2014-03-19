def findCapitalised(tweet):
	"""takes as input a list which contains words in tweet and return the percentage of capitalised words"""
	count=0
	for i in range(len(tweet)):
		if tweet[i].isupper():
			count+=1
	return float(count)/len(tweet)
