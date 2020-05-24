import praw
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import re

# TODO: incorporate multiple subreddits
#subreddit_list = ['askreddit', 'nba']

analyzer = SentimentIntensityAnalyzer()
store = {}
submission_urls = []
post_ids = []
titles = []
post_times = []
comments = []
upvote_counts = []


def process_comment(c):
    c = re.split("edit", c, flags=re.IGNORECASE)[0]
    return c


def predict_sentiment(s):
    return analyzer.polarity_scores(s)


reddit = praw.Reddit(client_id='xkCClYxt6N8Qng',
                     client_secret='P-QDxnqJqJ620o5IsTjDmi9ePvQ',
                     user_agent='vladtheinpaler')

subreddit = reddit.subreddit('askreddit')

for submission in subreddit.top("year", limit=10):
    print(submission.title)
    print(submission.id)
    print(submission.url)
    post_ids.append(submission.id)
    submission_urls.append(submission.url)
    titles.append(submission.title)
    post_times.append(submission.created_utc)
    upvote_counts.append(submission.score)

submission = reddit.submission(id=post_ids[0])
submission.comment_sort = 'hot'


for c in list(submission.comments):
    comments.append(process_comment(c))
