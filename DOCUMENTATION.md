# Viral Tweet Classifier

In the following text we will describe the process and overall pipeline of how to classify tweets into viral ones an non-viral ones. 

## Dataset

For our training and testing we will use the publicly availible dataset from (author). The data consist of n Tweets, all of whom are about the topic of data sience. Each data-point consist of the tweet content itsels and all the metainformation of that tweet such as, `images, retweets, likes, mentions, comments, place, language, etc.`.

The tweets will be labeld according to their virality. Virality in this case will be assigned by counting the likes, retweets, comments and weighing them accordingly. Tweets exceeding a predefined thershold of the weighted variables will be classified as viral and the ones below this threshold will be labeld non-viral.



## Evalaution

## Preprocessing

Before using the data we have to do some cleaning up and additionally some other preprocessing steps. For that we will run the datset into a pipeline containg multiple modules. These modules will then be run iteratively on the datset which will yield us a datset we can extract features for the classification from.



### Module 1: Punctuation Removal
The preprocessing will start with removing the punctioations from the tweets. This makes tokenization a lot easier and generall handling easier.

Example:
```
default: ''
result: ''
```

### Module 2: Stop Word Removal
Further we will remove stop words. These are words like `and, with, but` since these will occure in most of the tweets and don't yield any useful characteristic to base the classification on.

Example:
```
default: ''
result: ''
```

### Module 3: Removing Links
Since links most often only contain some cryptic url they will be replaced by a substitude token.

Example:
```
default: ''  
result: ''  
```

### Module 4: Lemmatization
The function of this module is to lemmatize the words in the tweet. Reducing the words in the tweets to their lemmas and additionally redcuing the variation between used words.

Example:
```
default: ''  
result: ''  
```

### Module 5: Tokenization
Within the last module the preprocessed tweets will be tokenized and every word will be set to an element within a newly created list instead of having a string as output.

Example:
```
default: 'some twees are viral some are not'  
result: '["some", "tweets", "are", "viral", "some", "are", "not"]'  
```

## Feature Selection

### Feature i: Tweet Sentiment
Given that polarizing opinions attract many listeners most of the times, we assume that the tweets with higher sentiment (either very positive or negative) will reach a larger audience. 


### Feature j: 


## Evaluation:

For the evaluation of the models simple scoring metrices will be used. The metrics are:  `accuracy, cohen_kappa, balanced_accuracy` and a `confusion matrix` of the classifications.

The reason for our usage of these metrices are that they are simple and when compared with each other a very good tool to esimate the abilities of the classifiers. 

To further the evaluation we will have a look at a later point at some **false positives** and **false negatives** to get a better understanding why the models acted the way they did.

## Classification

For the evaluation of the classification results we will create three runs. In each of these runs a different threshold for the virality will be set and classified by three different algorithms (Nearest Neighbor, SVM, Random Forest). 

### Run 1: 

**Like trehsold = 20**  
**Retweet trehsold = 20**  
**Comment trehsold = 20**  

image containing the results of classification

### Run 2:

**Like trehsold = 50**  
**Retweet trehsold = 50**  
**Comment trehsold = 50**  

image containing the results of classification

### Run 3:
**Like trehsold = 100**  
**Retweet trehsold = 100**  
**Comment trehsold = 100**  

image containing the results of classification


## Conclusion

The results have shown that the virality of a tweet is most often more complex than a few simple features. 













