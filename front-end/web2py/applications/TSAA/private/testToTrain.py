import time
while True:
    """sentence level"""
    rows = db(db.SentTestDetails.TrainStatus=='0').select()
    print rows
    for row in rows:
	tweet=row.Tweet
	token=row.Token
	label=row.ActualLabel

	print tweet
	print token
	print label

	row.update_record(TrainStatus='1')
	tid=db.SentTrainDetails.insert(Tweet=tweet, Token=token, Label=label)
        db.commit()

    """phrase level"""
    rows = db(db.PhraseTestDetails.TrainStatus=='0').select()
    print rows
    for row in rows:
	tweet=row.Tweet
	phrase=row.Phrase
	token=row.Token
	label=row.ActualLabel

	print tweet
	print phrase
	print token
	print label

	row.update_record(TrainStatus='1')
	tid=db.PhraseTrainDetails.insert(Tweet=tweet, Token=token, Label=label, Phrase=phrase)
        db.commit()
    time.sleep(60) # check every minute

    time.sleep(60) # check every minute
    db.commit()	
