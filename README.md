# twitter_politician_scraper

## Query meta data of a list of handles

        script/get_handle_meta_data.py

        Note: the handles are in twitter_handles/
        Note: this method can be used to verified a handle

## Query tweets of a list of handles after a given date

        script/get_tweet_after.py -- main
        script/tweet_dumper.py    -- utilities
        twitter_handles/          -- lists of politician handles        
        query_results/            -- query results      

        Note: you will need at least consumer_key and consumer_secret to run the code. 
        Note: twitter has a limit for the number of tweets returned by a single query. 
        The code keeps making new query from the end of the last query until reach the given the date or exhausting all tweets. 
        Note: the results in query_results/ are tweets for a governors, trump and his cabinet members, and the congress.
