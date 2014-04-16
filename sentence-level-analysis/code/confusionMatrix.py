import sys

positive=0
negative=1
neutral=2



"""

act/pred	positive negative neutral

positive	0 0	 0 1	  0 2
negative	1 0	 1 1	  1 2
neutral		2 0 	 2 1	  2 2

"""
if __name__ == '__main__':
	"""check arguments"""
	if len(sys.argv)!= 3:    
		print "Usage :: python .py actualLabels predictedLabels"
		sys.exit(0)

	actualFile=open(sys.argv[1],'r')
	predictedFile=open(sys.argv[2],'r')
	actualLabels=[]
	predictedLabels=[]
	confusionMatrix=[[0,0,0],[0,0,0],[0,0,0]]
	for i in actualFile:
		i=i.strip('\t\n\r ')
		actualLabels+=[i]

	for i in predictedFile:
		i=i.strip('\t\n\r ')
		predictedLabels+=[i]
	
	lenLabels=len(actualLabels)

	for i in range(lenLabels):
		confusionMatrix[eval(actualLabels[i])][eval(predictedLabels[i])]+=1
	print "actual/predicted\tpositive\tnegative\tneutral"
	print "positive\t\t",
	for i in confusionMatrix[positive]:
			print str(i)+'\t\t',
	print "\nnegative\t\t",
	for i in confusionMatrix[negative]:
			print str(i)+'\t\t',
	print "\nneutral\t\t\t",
	for i in confusionMatrix[neutral]:
			print str(i)+'\t\t',

	print		

