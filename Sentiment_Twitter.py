# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 14:26:42 2017

@author: Jason
"""
from nltk.corpus import twitter_samples
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier

twitter_samples.fileids()

#print tweets
strings = twitter_samples.strings('negative_tweets.json')
for string in strings[:5]:
    print(string)

print("\n")   
    
strings = twitter_samples.strings('positive_tweets.json')
for string in strings[:5]:
    print(string)

print("\n") 
    
def create_word_features(words):
    useful_words = [word for word in words if word not in stopwords.words('english')]
    my_dict = dict([(word,True) for word in useful_words])
    return my_dict
    
create_word_features(['the', 'quick', 'brown', 'the', 'jumps' , 'quick'])

#extract pos/neg tweets
neg_tweets = []
for string in twitter_samples.strings('negative_tweets.json'):
#for fileid in twitter_samples.fileids('jsons'):
    words = word_tokenize(string)
    neg_tweets.append((create_word_features(words),"negative"))
print(neg_tweets[0])
print(len(neg_tweets))
print("\n") 

pos_tweets = []
for string in twitter_samples.strings('positive_tweets.json'):
    words = word_tokenize(string)
    pos_tweets.append((create_word_features(words),"positive"))
print(pos_tweets[0])
print(len(pos_tweets))
print("\n") 

# Create the training and test set
train_set = neg_tweets[:750] + pos_tweets[:750]
test_set = neg_tweets[750:] + pos_tweets[750:]
print(len(train_set), len(test_set))

# Create a Naive bayes classifier
classifier = NaiveBayesClassifier.train(train_set)

# Find the accuracy
accuracy = nltk.classify.util.accuracy(classifier, test_set)
print(accuracy * 100)
print("\n") 

# Repeat the above code, this time replacing all smiley
neg_tweets = []
for string in twitter_samples.strings('negative_tweets.json'):
    string = (string.replace(":", "").replace(")", "").replace("(", ""))
    words = word_tokenize(string)
    neg_tweets.append((create_word_features(words),"negative"))
    
print(neg_tweets[0])
print(len(neg_tweets))
print("\n") 

pos_tweets = []
for string in twitter_samples.strings('positive_tweets.json'):
    string = (string.replace(":", "").replace(")", "").replace("(", ""))
    words = word_tokenize(string)
    pos_tweets.append((create_word_features(words),"positive"))
    
print(pos_tweets[0])
print(len(pos_tweets))
print("\n") 

# Create the training and test set
train_set = neg_tweets[:750] + pos_tweets[:750]
test_set = neg_tweets[750:] + pos_tweets[750:]
print(len(train_set), len(test_set))

# Create a Naive bayes classifier
classifier = NaiveBayesClassifier.train(train_set)

# Find the accuracy
accuracy2 = nltk.classify.util.accuracy(classifier, test_set)
print(accuracy2 * 100)