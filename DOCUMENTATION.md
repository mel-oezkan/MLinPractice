# Viral Tweet Classifier

In the following text we will describe the process and overall pipeline of how to classify tweets into viral ones an non-viral ones. 

## Dataset

For our training and testing we will use the publicly availible dataset from (author)

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
The 