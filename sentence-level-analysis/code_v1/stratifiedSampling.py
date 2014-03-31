import sys

def stratification(inputFile, outputFile):

	positiveTweet=[]
	neutralTweet=[]
	negativeTweet =[]
	f=open(inputFile,'r')
	for line in f:
		words = line.strip().split('\t')
		if words[3] == 'positive':
			positiveTweet.append(line)
		elif words[3] == 'negative':
			negativeTweet.append(line)
		else:
			neutralTweet.append(line)

	length = min(len(positiveTweet),len(negativeTweet),len(neutralTweet))
	positiveTweet = positiveTweet[:length]
	neutralTweet = neutralTweet[:length]
	negativeTweet = negativeTweet [:length]

	f=open(outputFile,'w')
	f.write(''.join(positiveTweet))
	f.write(''.join(negativeTweet))
	f.write(''.join(neutralTweet))
	f.close()

if __name__ == '__main__':
    
    """check arguments"""
    if len(sys.argv)!= 3:                                                   
        print "Usage :: python main.py ../dataset/finalTrainingInput.txt ../dataset/finalTestingInput"
        sys.exit(0)

    stratification(sys.argv[1], sys.argv[2])