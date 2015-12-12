import sys
if __name__ == '__main__':
    
    """check arguments"""
    if len(sys.argv)!= 3:                                                   
        print "Usage :: python findF1.py actualLabel predictedLabel"
        sys.exit(0)

    predictedLabel=[]
    actualLabel=[]

    f=open(sys.argv[1],'r')
    for line in f:
    	actualLabel.append(line.strip())
    f.close()

    f=open(sys.argv[2],'r')
    for line in f:
    	predictedLabel.append(line.strip())
    f.close()

    countPositiveA=0
    countNegativeA=0
    countNeutralA=0

    for i in xrange(len(actualLabel)):
    	if actualLabel[i]=='positive':
    		countPositiveA+=1
    	elif actualLabel[i]=='negative':
    		countNegativeA+=1
    	else:
    		countNeutralA+=1

    countPositiveP=0
    countNegativeP=0
    countNeutralP=0

    for i in xrange(len(predictedLabel)):
    	if predictedLabel[i]=='positive':
    		countPositiveP+=1
    	elif predictedLabel[i]=='negative':
    		countNegativeP+=1
    	else:
    		countNeutralP+=1

    truePPositive=0
    truePNegative=0
    truePNeutral=0
    for i in xrange(len(predictedLabel)):
    	if predictedLabel[i]=='positive':
    		if actualLabel[i]=='positive':
    			truePPositive+=1
    	elif predictedLabel[i]=='negative':
    		if actualLabel[i]=='negative':
    			truePNegative+=1
    	else:
    		if actualLabel[i]=='neutral':
    			truePNeutral+=1

    precisionPositive = truePPositive/float(countPositiveP)
    precisionNegative = truePNegative/float(countNegativeP)
    precisionNeutral = truePNeutral/float(countNeutralP)

    recallPositive = truePPositive/float(countPositiveA)
    recallNegative = truePNegative/float(countNegativeA)
    recallNeutral = truePNeutral/float(countNeutralA)

    f1Positive = (2*precisionPositive*recallPositive)/(precisionPositive+recallPositive)
    f1Negative = (2*precisionNegative*recallNegative)/(precisionNegative+recallNegative)
    f1Neutral = (2*precisionNeutral*recallNeutral)/(precisionNeutral+recallNeutral)

    print "Precision: Positive, Negative, Neutral"
    print f1Positive
    print f1Negative
    print f1Neutral

    print "Recall: Positive, Negative, Neutral"

    print recallPositive
    print recallNegative
    print recallNeutral

    print "Average F1 for Positive and Neutral"

    average = (f1Neutral+f1Positive)/2
    print average
