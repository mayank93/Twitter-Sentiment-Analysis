# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations
import os
from tokenizer import *
from settings import *

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################


#-----------------------Error Page-----------------------------------
#if java script dissabled
def error():
	        return dict()

#-----------------------Home Page------------------------------------
@auth.requires_login()
def index():
	
    	session.email=auth.user.email
    	print session.email
    	return dict()


@auth.requires_login()
def test():
	tid=request.args[0]
	testType=request.args[1]
	print tid,testType
        session.email=auth.user.email
        print session.email
	if testType=='Sentence':
		details=db(db.SentTestDetails.id == tid).select()[0]
	else:
		details=db(db.PhraseTestDetails.id == tid).select()[0]
		
	if request.vars.Submit:
		if testType=='Sentence':
			db(db.SentTestDetails.id==tid).update(ActualStatus='1', ActualLabel=request.vars.ActualLabel)
		else:
			db(db.SentTestDetails.id==tid).update(ActualStatus='1', ActualLabel=request.vars.ActualLabel)
		
		print request.vars
	db.commit()
	print details
        return dict(details=details,testType=testType)

@auth.requires_login()
def testDetails():
    	session.email=auth.user.email
    	print session.email
	sentDetails=db(db.SentTestDetails.UserEmail == session.email).select()
	total=0
	correct=0
	for row in sentDetails:
		if(row.PredictedLabel==row.ActualLabel):
			correct+=1
		total+=1
	if total==0:
		accuracySent=[0.0,0.0,0.0]
	else:
		accuracySent=[correct,total,(correct*100.0)/total]
	phraseDetails=db(db.PhraseTestDetails.UserEmail == session.email).select() 
	total=0
	correct=0
	for row in phraseDetails:
		if(row.PredictedLabel==row.ActualLabel):
			correct+=1
		total+=1
	if total==0:
		accuracyPhrase=[0.0,0.0,0.0]
	else:
		accuracyPhrase=[correct,total,(correct*100.0)/total]
	print sentDetails
	print phraseDetails
	return dict(sentDetails=sentDetails,phraseDetails=phraseDetails,accuracySent=accuracySent,accuracyPhrase=accuracyPhrase)

@auth.requires_login()
def addTest():
    	session.email=auth.user.email
    	print session.email
	if request.vars.Submit=='Submit' :
		TestName='N/A'
		Tweet=request.vars.Tweet
		TestType=request.vars.TestType
		Phrase=request.vars.Phrase
		print TestName
		print Tweet
		print TestType
		print Phrase
		# tokenizing tweet
		data=tokenize(Tweet)
		data=data.split('\t')
		TokenizedTweet=data[0]
		Token=data[1]
		if TestType=='Sentence':
			tid=db.SentTestDetails.insert(TestName=TestName,UserEmail=session.email,Tweet=TokenizedTweet,Token=Token)
		else:
			data=tokenize(Phrase)
			data=data.split('\t')
			TokenizedPhrase=data[0]
			Token=data[1]
			tid=db.PhraseTestDetails.insert(TestName=TestName,UserEmail=session.email,Tweet=TokenizedTweet,Phrase=TokenizedPhrase,Token=Token)
		db.commit()
		redirect(URL(r=request, f='testDetails'))
	return dict()

@auth.requires_login()
def upload():
    print request.vars

    if request.vars.Submit:
	dataFile=db.Upload.File.store(request.vars.DataFile.file, request.vars.DataFile.filename)	
	print dataFile
	response.flash = 'file uploaded'
	id = db.Upload.insert(DataType=request.vars.DataType,TestType=request.vars.TestType,UserEmail=session.email,File=dataFile)
	db.commit()
    return dict()


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request,db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
