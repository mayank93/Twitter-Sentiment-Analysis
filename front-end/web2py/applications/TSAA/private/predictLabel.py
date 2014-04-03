import time
while True:
    """sentence level"""
    rows = db(db.SentTestDetails.PredictedStatus=='0').select()
    print rows
    for row in rows:
	tweet=row.Tweet

	print tweet
	"""tokenize tweet """
	token=''
	"""predict label"""
	predictedLabel=''
        row.update_record(Token=token, PredictedLabel=predictedLabel, PredictedStatus='1')
        db.commit()

    """phrase level"""
    rows = db(db.PhraseTestDetails.PredictedStatus=='0').select()
    print rows
    for row in rows:
	tweet=row.Tweet
	phrase=row.Phrase

	print tweet
	print phrase
	"""tokenize tweet """
	token=''
	"""predict label"""
	predictedLabel=''
        row.update_record(Token=token, PredictedLabel=predictedLabel, PredictedStatus='1')
        db.commit()
    time.sleep(60) # check every minute
    db.commit()
