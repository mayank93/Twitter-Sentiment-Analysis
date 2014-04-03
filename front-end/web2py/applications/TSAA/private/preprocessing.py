from tokenizer import *
import time

while True:
    rows = db(db.Upload.ProcessedStatus=='0').select()
    """for phraseLevel file format is 'tweet\tphraseIndexStartingFrom0\tlabel"""
    """for sentenceLevel file format is 'tweet\tlabel"""
    """label in optional for test data"""

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
            for line in f:
                if line:
                    line=line.split('\t')
                    tweet=line[0].strip('\r\t\n ')
                    phrase=tweet[int(line[1]):int(line[2])+1]
                    label=''
                    if len(line)>3:
                        label=line[3].strip('\r\t\n ')
                    data=tokenize(tweet)
                    data=data.split('\t')
                    tokenizedTweet=data[0]
                    token=data[1]
                    if row.DataType=='Train':
                        if label:
                            tid=db.PhraseTrainDetails.insert(Tweet=tokenizedTweet, Token=token, Label=label,Phrase=phrase,UserEmail=row.UserEmail)
                    else:
                        if label:
                            tid=db.PhraseTestDetails.insert(Tweet=tokenizedTweet, Token=token, ActualLabel=label, ActualStatus='1',Phrase=phrase,UserEmail=row.UserEmail)
                        else:
                            tid=db.PhraseTestDetails.insert(Tweet=tokenizedTweet, Token=token, Phrase=phrase,UserEmail=row.UserEmail)
                    db.commit()
        row.update_record(ProcessedStatus='1')
        db.commit()
    time.sleep(60) # check every minute
