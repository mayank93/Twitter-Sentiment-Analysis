"""This code takes as input the path of the filename of the original dataset and the output filename"""
"""It returns the processed dataset with the relevant fields"""
"""It helps in generating Training Data with Labels and Testing Data with Labels or without labels"""


import sys

def main():    

    """check arguments"""
    if len(sys.argv)!= 4:                                                                               
        print "Usage :: python extractData pathOfInputFileName outputFileName tempFileToHoldTweetForNlpTagger"
        sys.exit(0)

    """Cherry Pick"""
    data=[]
    data1=[]
    f=open(sys.argv[1],'r')
    for line in f:
    	words = line.split('\t')
        if words[3]!="Not Available\n":
            #startIndex = int(words[2])
            #endIndex = int(words[3])+1
            #string = words[5].split(' ')
            #phrase = ' '.join(string[startIndex:endIndex]).strip('\n')
           #use appropriate lines comment either of the lines
    	   data.append(line) #with labels
           # data.append(words[0]+'\t'+words[1]+'\t'+phrase+'\t'+words[4])
           # data1.append(phrase)
           #data.append(words[0]+'\t'+words[3])#without labels
           data1.append(words[3])
    f.close()

    """write into file"""
    f=open(sys.argv[2],'w')
    f.write("".join(data))
    f.close()

    f=open(sys.argv[3],'w')
    f.write("".join(data1))
    f.close()
if __name__ == "__main__":                                                                              
    main()
