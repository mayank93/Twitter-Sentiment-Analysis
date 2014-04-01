import sys

if __name__ == '__main__':
    uniTweet={}
    f=open(sys.argv[1],'r')
    for i in f:
        if i:
            i=i.split('\t')
            label
            tweet=i[3]
            uniTweet[tweet]=0
    for i in uniTweet.keys():
        print i
    f.close()

