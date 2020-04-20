################################
# twitter scrapers
#################################

import tweepy
import csv
import datetime

#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

####################################################################################################
# exhaust a users most recent tweets (twitter has set a limit for this, not sure the exact number)
###################################################################################################
def get_all_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    #auth.set_access_token(access_key, access_secret) # not necessary, but uncomment it if have access_key
    api = tweepy.API(auth)

    #initialize a list to hold all the tweepy Tweets
    alltweets = []

    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,tweet_mode='extended',count=200)

    #save most recent tweets
    alltweets.extend(new_tweets)

    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    #keep grabbing tweets until there are no tweets left to grab
    while len(alltweets) < 1000:
        print "getting tweets before %s" % (oldest)

        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,tweet_mode='extended',count=200,max_id=oldest)

        #save most recent tweets
        alltweets.extend(new_tweets)

        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print "...%s tweets downloaded so far" % (len(alltweets))

    #transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [[tweet.id_str, tweet.created_at, tweet.full_text.encode("utf-8")] for tweet in alltweets]

    #write the csv
    with open('%s_tweets.csv' % screen_name, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text"])
        writer.writerows(outtweets)

##################################################################
# get a users tweets after a given date
# may write an empty file, if no tweets after the given date
##################################################################
def get_all_tweets_by(screen_name, start_date, save_path='./'):
    #Twitter only allows access to a users most recent 3240 tweets with this method

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    #auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #initialize a list to hold all the tweepy Tweets
    alltweets = []

    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,tweet_mode='extended',count=200)

    #save most recent tweets
    alltweets.extend(new_tweets)

    if len(alltweets) > 0:
        #save the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        # the time the oldest tweet created
        oldest_time = alltweets[-1].created_at

        #keep grabbing tweets until there are no tweets left to grab
        # or the start date is reached
        while oldest_time > start_date:
            #print "getting tweets before %s" % (oldest)
            print('getting tweets before %s' % (oldest_time.strftime('%Y-%m-%d')))
            #all subsiquent requests use the max_id param to prevent duplicates
            new_tweets = api.user_timeline(screen_name = screen_name,tweet_mode='extended',count=200,max_id=oldest)

            if len(new_tweets) == 0:
                break

            #save most recent tweets
            alltweets.extend(new_tweets)

            #update the id of the oldest tweet less one
            oldest = alltweets[-1].id - 1

            oldest_time = alltweets[-1].created_at
            print "...%s tweets downloaded so far" % (len(alltweets))

        #transform the tweepy tweets into a 2D array that will populate the csv
        outtweets = [[tweet.id_str, tweet.created_at, tweet.full_text.encode("utf-8")] for tweet in alltweets if tweet.created_at >= start_date]

        #write the csv
        with open(save_path + '%s_tweets_after_%s.csv' % (screen_name,start_date.strftime('%Y-%m-%d')), 'wb') as f:
            writer = csv.writer(f)
            writer.writerow(["id","created_at","text"])
            writer.writerows(outtweets)
    else:
        print('%s has no tweets after %s' % (screen_name, start_date.strftime('%Y-%m-%d')))


if __name__ == '__main__':

    start_date = datetime.datetime(2020, 4, 1, 0, 0, 0)

    #pass in the username of the account you want to download
    #get_all_tweets("realdonaldtrump")
    get_all_tweets_by('realdonaldtrump', start_date)



