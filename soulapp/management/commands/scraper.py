import praw
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import re
import time
from datetime import datetime


class Scraper():
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()
        self.data = {}
        self.reddit = praw.Reddit(client_id='xkCClYxt6N8Qng',
                                  client_secret='P-QDxnqJqJ620o5IsTjDmi9ePvQ',
                                  user_agent='vladtheinpaler')
        self.subreddit_list = pd.read_csv("subreddit_list.csv")['subreddit']

    def process_comment(self, c):
        c = re.split(" edit", c, flags=re.IGNORECASE)[0]
        return c

    def analyze_submission(self, id):
        submission = self.reddit.submission(id=id)
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
        sentiment_value = sentiment / num_comments if sentiment else 0
        print("overall sentiment: ", sentiment_value)
        self.data[id]['sentiment_value'] = sentiment_value

    def predict_sentiment(self, s):
        sentiment = self.analyzer.polarity_scores(s)
        sentiment = sentiment['pos'] - sentiment['neg']
        print('sentiment: ', sentiment)
        return sentiment

    def process_subreddit(self, sub_name):
        subreddit = self.reddit.subreddit(sub_name)
        for sub in subreddit.top("year", limit=3):
            print("post:", sub.title, "|", sub.url)
            self.data[sub.id] = {
                'id': sub.id,
                'subreddit': sub_name,
                'url': sub.url,
                'title': sub.title,
                'date': datetime.fromtimestamp(sub.created_utc),
                'upvote_count': sub.score
            }
            self.analyze_submission(sub.id)

    def load_data(self):
        for sub in self.subreddit_list:
            print("processing:", sub)
            self.process_subreddit(sub)
            print(sub, "processed")
            print("waiting...")
            time.sleep(4)

    def write_data(self):
        data = pd.DataFrame.from_dict(self.data, orient='index')
        data.to_csv("data.csv")

    def get_data(self):
        return pd.DataFrame.from_dict(self.data, orient='index')

    def save_data(self, data):
        pass
