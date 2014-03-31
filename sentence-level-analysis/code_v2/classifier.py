from svmutil import *
from sklearn import naive_bayes
from sklearn.externals import joblib

def svmClassifier(trainingLabel,testingLabel,featureVectorsTrain,featureVectorsTest):
    
    """Feed the feature vector to svm to create model"""
    print "Creating SVM Model"
    model= svm_train(trainingLabel,featureVectorsTrain)
    print "Model created. Saving..."

    """Save model"""
    svm_save_model('sentimentAnalysisSVM.model', model)
    print "Model Saved. Proceed to test..."

    predictedLabel, predictedAcc, predictedValue = svm_predict(testingLabel, featureVectorsTest, model)
    print "Finished. The accuracy is:"
    print predictedAcc[0]
    return predictedLabel

def naiveBayesClassifier(trainingLabel,testingLabel,featureVectorsTrain,featureVectorsTest):
    """Feed the feature vector to svm to create model"""
    print "Creating Naive Bayes Model"
    mnb = naive_bayes.GaussianNB()
    mnb.fit(featureVectorsTrain,trainingLabel)
    print "Model created. Saving..."
    
    """Save model"""
    joblib.dump(mnb, 'sentimentAnalysisNaiveBayes.pkl', compress=9)
    print mnb.score(featureVectorsTest,testingLabel)
