import praw
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import re

subreddit_list = ['askreddit']

analyzer = SentimentIntensityAnalyzer()
data = {}
reddit = praw.Reddit(client_id='xkCClYxt6N8Qng',
                     client_secret='P-QDxnqJqJ620o5IsTjDmi9ePvQ',
                     user_agent='vladtheinpaler')


def process_comment(c):
    #print('c: ', c)
    c = re.split("edit", c, flags=re.IGNORECASE)[0]
    return c


def analyze_submission(id):
    submission = reddit.submission(id=id)
    submission.comment_sort = 'hot'
    sentiment = 0
    num_comments = 0
    for c in list(submission.comments):
        try:
            comment = process_comment(c.body)
            print('comment: ', comment)
            sentiment += predict_sentiment(comment)
            num_comments += 1
        except:
            pass
    data[id]['sentiment_value'] = sentiment / num_comments


def predict_sentiment(s):
    sentiment = analyzer.polarity_scores(s)
    print('sentiment: ', sentiment)
    return sentiment['compound']


def process_subreddit(subreddit):
    subreddit = reddit.subreddit('askreddit')
    for sub in subreddit.top("year", limit=10):
        # print(submission.title)
        # print(submission.id)
        # print(submission.url)
        data[sub.id] = {
            'url': sub.url,
            'title': sub.title,
            'post_time': sub.created_utc,
            'upvote_count': sub.score
        }


def load_data():
    for sub in subreddit_list:
        process_subreddit(sub)
