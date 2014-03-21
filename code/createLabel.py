import sys

def main():    
    if len(sys.argv)!= 3:                                                                               #check arguments
        print "Usage :: python createLabel.py pathOfInputFileName outputFileName"
        #python createLabel.py ../documents-export-2014-03-19/trainingDatasetProcessed.txt ../documents-export-2014-03-19/trainingLabel.txt
        #python createLabel.py ../documents-export-2014-03-19/testingDatasetProcessed.txt ../documents-export-2014-03-19/testinglabel.txt
        sys.exit(0)

    encode={'positive': '1','negative': '-1','neutral':'0'}
    data=[]
    f=open(sys.argv[1],'r')
    for line in f:
    	words = line.split('\t')
        if words[3]!="Not Available\n":
           data.append(encode[words[2]]+'\n')
    f.close()

    f=open(sys.argv[2],'w')
    f.write("".join(data))
    f.close()

if __name__ == "__main__":                                                                               #main
    main()