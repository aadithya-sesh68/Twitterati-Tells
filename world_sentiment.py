import tweepy
from textblob import TextBlob
import preprocessor as p
import statistics
from typing import List

consumer_key=""
consumer_secret=""

def get_tweets(keyword: str) -> List[str]:
    all_tweets = []
    for tweet in tweepy.Cursor(api.search, q=keyword, tweet_mode='extended', lang='en').items(10):
        all_tweets.append(tweet.full_text)

    return all_tweets

def clean_tweets(all_tweets: List[str]) -> List[str]:
    tweets_clean=[]
    for tweet in all_tweets:
        tweets_clean.append(p.clean(tweet))

    return tweets_clean

def get_sentiment(cleaned_tweets: List[str]) -> List[float]:
    sentiment_scores = []
    for tweet in cleaned_tweets:
        blob = TextBlob(tweet)
        sentiment_scores.append(blob.sentiment.polarity)

    return sentiment_scores

def generate_average_sentiment_score(keyword: str) -> int:
    tweets = get_tweets(keyword)
    cleaned_tweets = clean_tweets(tweets)
    sentiment_scores = get_sentiment(cleaned_tweets)

    avg_score = statistics.mean(sentiment_scores)

    return avg_score

if __name__ == "__main__":
    print("What do the Tweeples prefer?")
    first_thing = input()
    print("...or...")
    second_thing = input()
    print("\n")

    first_score = generate_average_sentiment_score(first_thing)
    second_score = generate_average_sentiment_score(second_thing)

    if(first_score > second_score):
        print(f"#Twitterati Tweeples prefer {first_thing} over {second_thing} !!")
    else:
        print(f"#Twitterati Tweeples prefer {second_thing} over {first_thing} !!")