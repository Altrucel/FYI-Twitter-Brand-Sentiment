# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 01:53:21 2017

@author: Jason
"""
#oauth
import csv
import os
import tweepy
from tweepy.error import TweepError
from tweepy import OAuthHandler
import json
#import sys
#from tweepy import Cursor
#from twitter_client import get_twitter_client

#path directories
work_dir = os.getcwd()
work_path = "\jsons"
data_path = work_dir+work_path
if not os.path.exists(data_path):
    os.mkdir(data_path)
#api credentials
consumer_key = 'rP3UrR6kVcYvwUXTRU1VxhwUv'
consumer_secret = '6djqRw8xl7Dv0ZJ7mjwUTY59h99yLM8ko0y2Gy1I4wDHsstha8'
access_token = '915650793834815489-3QfDCTE7CbRARrSfSnHTgT5iWkU7GBR'
access_secret = '0Z1WJRHoLMoZMaYruRne0OnI6FwhaljHa1SRqXrGPrD0G'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify =True)
def make_filename(some_name):
    return (data_path+"\\"+some_name+".json")

def process_or_store(path, name):
    #print(json.dumps(tweet))
    with open(path,'w') as f:
        try:
            for tweet in tweepy.Cursor(api.user_timeline, screen_name=name, count=200).items():
                f.write(json.dumps(tweet._json)+"\n")
        except tweepy.TweepError as e:
            print (e.api_code)
           #print(tweepy.TweepError)
            print ("User not found")
            pass

#generates list from a csv
tweetlist = []
with open ('influencers.csv', newline='') as csvfile:
        tweetreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in tweetreader:
                tweetlist.append(row[0]) 
                
for name in tweetlist:
    process_or_store(make_filename(name),name)

