from tokenizer import *
import time

while True:
    rows = db(db.Upload.ProcessedStatus=='0').select()
    """for phraseLevel file format is 'tweet\tphraseIndexStarting\tphraseIndexEnging\tlabel"""
    """for sentenceLevel file format is 'tweet\tlabel"""
    """label in optional for test data"""
    """indexing from 0"""

    for row in rows:
        cwd=os.getcwd()
        fileName = os.path.join(appPath, 'uploads', row.File)
        f=open(fileName,'r')
        if row.TestType=='Sentence':
            for line in f:
                if line:
                    line=line.split('\t')
                    tweet=line[0].strip('\r\t\n ')
                    label=''
                    if len(line)>1:
                        label=line[1].strip('\r\t\n ')
                    data=tokenize(tweet)
                    data=data.split('\t')
                    tokenizedTweet=data[0]
                    token=data[1]
                    print label
                    if row.DataType=='Train':
                        if label:
                            tid=db.SentTrainDetails.insert(Tweet=tokenizedTweet, Token=token, Label=label,UserEmail=row.UserEmail)
                    else:
                        if label:
                            tid=db.SentTestDetails.insert(TestName='N/A',Tweet=tokenizedTweet, Token=token, ActualLabel=label, ActualStatus='1',UserEmail=row.UserEmail)
                        else:
                            tid=db.SentTestDetails.insert(TestName='N/A',Tweet=tokenizedTweet, Token=token,UserEmail=row.UserEmail)
                    print tid
                    db.commit()
                    
        else:
	    ii=0
            for line in f:
                if line:
                    line=line.split('\t')
                    tweet=line[0].strip('\r\t\n ')
		    tweet=tweet.split()
                    phrase=tweet[int(line[1]):int(line[2])+1]
		    tweet=' '.join(tweet)
		    phrase=' '.join(phrase)
                    label=''
                    if len(line)>3:
                        label=line[3].strip('\r\t\n ')
		    print tweet
		    print"-----------"
		    print phrase
		    print"-----------"
		    if phrase:
                    	data=tokenize(phrase)
                    	data=data.split('\t')
                    	tokenizedTweet=data[0]
                    	token=data[1]
		    	print token
                    	if row.DataType=='Train':
                        	if label:
                            		tid=db.PhraseTrainDetails.insert(Tweet=tweet, Token=token, Label=label,Phrase=tokenizedTweet,UserEmail=row.UserEmail)
                    	else:
                        	if label:
                            		tid=db.PhraseTestDetails.insert(TestName='N/A',Tweet=tweet, Token=token, ActualLabel=label, ActualStatus='1',Phrase=tokenizedTweet,UserEmail=row.UserEmail)
                        	else:
                            		tid=db.PhraseTestDetails.insert(TestName='N/A',Tweet=tweet, Token=token, Phrase=tokenizedTweet,UserEmail=row.UserEmail)
                    	db.commit()
        row.update_record(ProcessedStatus='1')
        db.commit()
    time.sleep(60) # check every minute
