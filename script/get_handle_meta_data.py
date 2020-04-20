######################################################
# scan a list of twitter handles
# return meta data of a handle if it is valid
######################################################
import tweepy
from tweepy import Cursor
import unicodecsv
from unidecode import unidecode
import pandas as pd

name = 'trump_cabinet_twitter_handles_clean'

# load politician handles
politicians = pd.read_csv('twitter_handles/%s.csv' % (name))

# Authentication and connection to Twitter API.
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# Usernames whose tweets we want to gather.
users = politicians['handle'].values



with open('%s.meta' % (name), 'wb') as file:
    writer = unicodecsv.writer(file, delimiter = ',', quotechar = '"')
    # Write header row.
    writer.writerow(["name",
                    "username",
                    "followers_count",
                    "listed_count",
                    "following",
                    "favorites",
                    "verified",
                    "default_profile",
                    "location",
                    "time_zone",
                    "statuses_count",
                    "description",
                    "geo_enabled",
                    "contributors_enabled",
                    "created_at"])

    for user in users:
        try:
            user_obj = api.get_user(user)

            # Gather info specific to the current user.
            user_info = [user_obj.name,
                         user_obj.screen_name,
                         user_obj.followers_count,
                         user_obj.listed_count,
                         user_obj.friends_count,
                         user_obj.favourites_count,
                         user_obj.verified,
                         user_obj.default_profile,
                         user_obj.location,
                         user_obj.time_zone,
                         user_obj.statuses_count,
                         user_obj.description,
                         user_obj.geo_enabled,
                         user_obj.contributors_enabled,
                         user_obj.created_at]

            writer.writerow(user_info)
        except:
            print('%s not found' % (user))
