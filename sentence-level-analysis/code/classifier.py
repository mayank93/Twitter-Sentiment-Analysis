from svmutil import *

def svmClassifier(trainingLabel,testingLabel,featureVectorsTrain,featureVectorsTest):
    
    """Feed the feature vector to svm to create model"""
    print "Creating SVM Model"
    model= svm_train(trainingLabel,featureVectorsTrain)
    print "Model created. Saving..."

    """Save model"""
    svm_save_model('.//code//sentimentAnalysisSVM.model', model)
    print "Model Saved. Proceed to test..."

    predictedLabel, predictedAcc, predictedValue = svm_predict(testingLabel, featureVectorsTest, model)
    print "Finished. The accuracy is:"
    print predictedAcc[0]
    return predictedLabel
