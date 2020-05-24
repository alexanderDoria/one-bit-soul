import praw
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import re
import time

subreddit_list = ['askreddit', 'nba']

analyzer = SentimentIntensityAnalyzer()
data = {}
reddit = praw.Reddit(client_id='xkCClYxt6N8Qng',
                     client_secret='P-QDxnqJqJ620o5IsTjDmi9ePvQ',
                     user_agent='vladtheinpaler')


def process_comment(c):
    c = re.split(" edit", c, flags=re.IGNORECASE)[0]
    return c


def analyze_submission(id):
    submission = reddit.submission(id=id)
    submission.comment_sort = 'hot'
    sentiment = 0
    num_comments = 0
    for c in list(submission.comments):
        try:
            comment = process_comment(c.body)
            #print('comment: ', comment)
            sentiment += predict_sentiment(comment)
            num_comments += 1
        except:
            pass
    sentiment_value = sentiment / num_comments if sentiment != 0 else 0
    data[id]['sentiment_value'] = sentiment_value


def predict_sentiment(s):
    sentiment = analyzer.polarity_scores(s)
    sentiment = sentiment['pos'] - sentiment['neg']
    #print('sentiment: ', sentiment)
    return sentiment


def process_subreddit(sub):
    subreddit = reddit.subreddit(sub)
    for sub in subreddit.top("year", limit=25):
        print(sub.title, "|", sub.url)
        data[sub.id] = {
            'id': sub.id,
            'url': sub.url,
            'title': sub.title,
            'post_time': sub.created_utc,
            'upvote_count': sub.score
        }
        analyze_submission(sub.id)


def load_data():
    for sub in subreddit_list:
        print("processing:", sub)
        process_subreddit(sub)
        print(sub, "processed")
        print("waiting...")
        time.sleep(4)


load_data()
