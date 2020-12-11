import tweepy
import pandas as pd
import json
from flatten_json import flatten
from pandas import DataFrame
import click


@click.command()
@click.option('--file', prompt='Name of File without .jsonl',
              help='Name of File without .jsonl')
@click.option('--cnt', prompt='Number of tweets',
              help='Take first n tweets to convert to CSV.')
def create(file, cnt):
    tweets_data = []
    with open(file + '.jsonl', "r") as tweets_file:
        # Read in tweets and store in list
        for line in tweets_file:
            tweet = json.loads(line)
            tweet = flatten(tweet)
            tweets_data.append(tweet)

    tweet_json = json.dumps(tweets_data)

    with open(file + '_flatten_file.json', 'w') as f:
        f.write(tweet_json)

    with open(file + '_flatten_file.json') as json_file:
        data_csv = pd.read_json(json_file)

    with open(file + '_all_.csv', 'w') as f:
        data_csv.to_csv(f, index=False)

    with open(file + '_first_'+str(cnt)+'_tweets.csv', 'w') as f:
        data_csv.head(int(cnt)).to_csv(f, index=False)

    print("Three files have been created on the same folder: \n" +
            "------------------------------------------------- \n" +
          file + '_flatten_file.json \n' +
          file + '_all_.csv \n' +
          file + '_first_'+str(cnt)+'_tweets.csv \n' +
          "------------------------------------------------- \n")

if __name__ == '__main__':
    create()
