import time
while True:
    rows = db(db.TestDetails.MailSent=='false').select()
    print rows
    for row in rows:
        subject='My Tester testing Complete'
        if row.Status=='3':
            message='Hi  '+ row.UserEmail.split('@')[0]+'\n    Your test job for url '+ row.Url +' was completed successfully. You can view the report by clicking the following link: '+host+'/FunkLoad/default/test/'+str(row.id)+'  .\n\n\nCheers\nTeam FunkloadApp \n'
            
        elif row.Status>'3':
            message='Hi  '+ row.UserEmail.split('@')[0]+'\n    Your test job for url '+ row.Url +' encountered an unknown error. Please review the test parameters, or try submitting the request again.\n\n\nCheers\nTeam FunkloadApp \n'
        else:
            continue
        print message
        print row.id
        if mail.send(to=row.UserEmail,subject=subject,message=message):
            row.update_record(MailSent='true')
        else:
            row.update_record(MailSent='failed')
        db.commit()
    time.sleep(60) # check every minute
    db.commit()
