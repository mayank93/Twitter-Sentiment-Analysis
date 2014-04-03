#when u want to train the model again run this

"""
from testing import test as testingTest
from PhraseLevel import test as PhraseTest
from SentenceLevel import test as PhraseTest

testingTest.a()
"""

""" sentence level model """
rows = db(db.SentTrainDetails.id>0).select()
print rows
"""get unique tweets and make uni,bi,tri gram model """

"""for each row extract the tweet,token,label and do preprocesing and create a feature vector"""

"""feed feature vector to svm to get model save it"""


""" phrase level model """
"""get unique tweets and make uni,bi,tri gram model """
rows = db(db.PhraseTrainDetails.id>0).select()
print rows
"""for each row extract the tweet,phrase,token,label and do preprocesing and create a feature vector"""

"""feed feature vector to svm to get model"""
