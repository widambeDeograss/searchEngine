import snscrape.modules.twitter as sntwitter
import pandas as pd
import os
import requests


class Twitter:
    def __init__(self, username, number):
        self.tweet_data = []
        self.username = username
        self.number = number


    def get_tweets(self):
        for i, tweets in enumerate(sntwitter.TwitterSearchScraper('{}'.format(self.username)).get_items()):
            if i > self.number:
                break
            self.tweet_data.append(
                [tweets.date, tweets.content, tweets.user.username, tweets.url, tweets.media, tweets.hashtags,
                 tweets.mentionedUsers, tweets.coordinates, tweets.place, tweets.replyCount, tweets.retweetCount,
                 tweets.quotedTweet, tweets.lang, tweets.sourceUrl, tweets.sourceLabel])

            df = pd.DataFrame(self.tweet_data,
                              columns=['Date', 'Tweets', 'Username', 'Url', 'Media', 'Hashtags', 'MentionedUsers',
                                       'Coordinates', 'Place', 'ReplyCount', 'RetweetCount', 'QuotedTweet', 'Lang',
                                       'SourceUrl', 'SourceLabel'])
            df.to_csv(f'{self.username}.csv', index=False, encoding='utf-8')
        return f'/home/{self.username}'



