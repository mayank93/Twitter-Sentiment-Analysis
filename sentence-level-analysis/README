Sub Task B: Message Polarity Classification
Given a message, classify whether the message is of positive, negative, or neutral sentiment. For messages conveying both a positive and negative sentiment, whichever is the stronger sentiment should be chosen.


Files Info:

1. ./dataset/<train/test>ingDatasetComplete.txt
Contains complete <train/test>ing dataset in following format:
<tweetID>"\t"<ID>"\t"<label>"\t"<tweet>

2. ./dataset/<train/test>ingDatasetProcessed.txt
Contains processed <train/test>ing dataset without the entries for which tweet are not available in following format:
<tweetID>"\t"<ID>"\t"<label>"\t"<tweet>

3. ./dataset/example_tweets.txt
Temporary File To Hold Tweets For NLP POS Tagger in following format:
<tweet>

4. ./dataset/<train/test>ingTokenised.txt
File created after running NLP POS Tagger on dataset in following format
<tokens>"\t"<POSTags>"\t"<TagValues>"\t"<tweet>

5. ./dataset/final<Train/Test>ingInput.txt
Combine <train/test>ingDatasetProcessed.txt <train/test>ingTokenised.txt to create dataset/final<Train/Test>ingInput.txt which contains tagged tweets with  their labels in follwing format:
<tweetID>"\t"<tweet>"\t"<POSTags>"\t"<label>

6. ./code/taskB.gs
Contains actual labels for the tweets in dataset/testingTokenised.txt

7. ./code/taskB.pred
Contains predicted labels for the tweets in dataset/testingTokenised.txt

Run Following Commands: 

1. Remove entries from tranning dataset for which tweet is not available
$python ./code/extractDataset.py ./dataset/trainingDatasetComplete.txt ./dataset/trainingDatasetProcessed.txt ./dataset/example_tweets.txt

2. POS tagging training dataset
$./ark-tweet-nlp/runTagger.sh ./dataset/example_tweets.txt > ./dataset/trainingTokenised.txt

3. Combine trainingDatasetProcessed.txt trainingTokenised.txt to create dataset/finalTrainingInput.txt which contains tagged 
tweets with their labels
$python ./code/combine.py ./dataset/trainingDatasetProcessed.txt ./dataset/trainingTokenised.txt ./dataset/finalTrainingInput.txt

4. Remove entries from testing dataset for which tweet is not available
$python ./code/extractDataset.py ./dataset/testingDatasetComplete.txt ./dataset/testingDatasetProcessed.txt ./dataset/example_tweets.txt

5. POS tagging testing dataset
$./ark-tweet-nlp/runTagger.sh ./dataset/example_tweets.txt > ./dataset/testingTokenised.txt

6.Combine testingDatasetProcessed.txt testingTokenised.txt to create dataset/finalTestingInput.txt which contains tagged tweets 
with their label
$python ./code/combine.py ./dataset/testingDatasetProcessed.txt ./dataset/testingTokenised.txt ./dataset/finalTestingInput.txt

7. Train the model on ./dataset/finalTrainingInput.txt and test it on /dataset/finalTestingInput.txt, generating 
./code/taskB.gs ./code/taskB.pred 
$python ./code/main.py ./dataset/finalTrainingInput.txt ./dataset/finalTestingInput.txt

8. Finds precison and recall
$python ./code/findf1.py ./code/taskB.gs ./code/taskB.pred
