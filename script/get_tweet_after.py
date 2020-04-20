#################################################
# get tweets from a list of politicians
################################################

import pandas as pd
import tweepy
import csv
import datetime
from tweet_dumper import *


if __name__ == '__main__':
    #df = pd.read_csv('../twitter_handles/trump_cabinet_twitter_handles_clean.csv')
    df = pd.read_csv('../twitter_handles/governors_2020_twitter_handles_clean.csv')
    #df = pd.read_csv('../twitter_handles/congress_116_twitter_handles_clean.csv')

    save_path = '../query_results/trump_and_cabinet/'
    #save_path = '../query_results/governors/'
    #save_path = './query_results/congress/'
    start_date = datetime.datetime(2020, 1, 1, 0, 0, 0)

    user_list = df['handle'].values

    #pass in the username of the account you want to download
    #get_all_tweets("realdonaldtrump")

    # get tweets for a list of handles
    for i in range(len(user_list)):
        user_name = user_list[i][1:] # get rid of @
        get_all_tweets_by(user_name, start_date, save_path)




