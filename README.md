# twitter_politician_scraper

## Query meta data of a list of handles

        script/get_handle_meta_data.py

Note: the handles are in twitter_handles/
Note: this method can be used to verify handles

## Query tweets of a list of handles after a given date

        script/get_tweet_after.py -- main
        script/tweet_dumper.py    -- utilities
        twitter_handles/          -- lists of politician handles        
        query_results/            -- query results      

Note: you will need at least consumer_key and consumer_secret to run the code. 
Note: twitter has a limit for the number of tweets returned by a single query. The code keeps making new query from the end of the last query until reach the given the date or exhausting all tweets. 
Note: the results in query_results/ are tweets for a governors, trump and his cabinet members, and the congress.

## Cite
This dataset contains tweets of high profile politicians during the coronavirus outbreak (Jan 1, 2020 ~ April 7, 2020). The dataset is used in the following paper. If you have used the dataset, please cite:
        
Sha, H.; Al Hasan, M.; Mohler, G.; and Brantingham, P.J. Dynamic topic modeling of the COVID-19 Twitter narrative among U.S. governors and cabinet executives.
