"""This code takes as input the path of the filename of the original dataset and the output filename"""
"""It returns the processed dataset with the relevant fields"""
"""It helps in generating Training Data with Labels and Testing Data with Labels or without labels"""


import sys

def main():    

    """check arguments"""
    if len(sys.argv)!= 3:                                                                               
        print "Usage :: python extractData pathOfInputFileName outputFileName"
        sys.exit(0)

    """Cherry Pick"""
    data=[]
    f=open(sys.argv[1],'r')
    for line in f:
    	words = line.split('\t')
        if words[3]!="Not Available\n":

           #use appropriate lines comment either of the lines
    	   #data.append(line) #with labels
           data.append(" ".join(words[3:]))
           #data.append(words[0]+'\t'+words[3])#without labels
    f.close()

    """write into file"""
    f=open(sys.argv[2],'w')
    f.write("".join(data))
    f.close()

if __name__ == "__main__":                                                                              
    main()