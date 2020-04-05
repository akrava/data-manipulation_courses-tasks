import sys
import json
import operator


def process_tweet(tweet_file):
    hashtags = {}
    for line in tweet_file:
        json_data = json.loads(line)
        if 'entities' not in json_data or 'hashtags' not in json_data['entities']:
            continue
        for hashtag_obj in json_data['entities']['hashtags']:
            if 'text' not in hashtag_obj:
                continue
            hashtag = hashtag_obj['text']
            hashtags[hashtag] = 1 + (hashtags[hashtag] if hashtag in hashtags else 0)
    tweet_file.seek(0)
    return hashtags


def main():
    tweet_file = open(sys.argv[1])
    hashtags = process_tweet(tweet_file)
    hashtags = sorted(hashtags.items(), key=operator.itemgetter(1), reverse=True)
    count_max = 10
    for term in hashtags:
        count_max -= 1
        if count_max < 0:
            return
        print term[0], term[1]


if __name__ == '__main__':
    main()
