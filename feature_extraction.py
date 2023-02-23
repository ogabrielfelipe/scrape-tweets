import pandas as pd
import re  

csv_tweets = pd.DataFrame(pd.read_csv('output_tweet_consolidated_sliced.csv', sep=';', header=None))[1][1:]

list_tweets = []
for tweet in csv_tweets:
    #Whether the tweet has hashtag
    hashtagInTweet =  [t for t in tweet.split() if t.startswith("#")]
    hashtagInTweetIsNotEmpty = len(hashtagInTweet) != 0
    totalHashtagInTweet = len(hashtagInTweet)
    print(hashtagInTweet, hashtagInTweetIsNotEmpty, totalHashtagInTweet)


    #Whether the tweet has mentions
    mentionInTweet =  [t for t in tweet.split() if t.startswith("@")]
    mentionInTweetIsNotEmpty = len(mentionInTweet) != 0
    totalMentionInTweet = len(mentionInTweet)    
    print(mentionInTweet, mentionInTweetIsNotEmpty, totalMentionInTweet)
    

    #Whether the tweet has URL
    urlInTweet =  [t for t in tweet.split() if re.findall('http\S+', t)]
    urlInTweetIsNotEmpty = len(urlInTweet) != 0
    totalUrlInTweet = len(urlInTweet)
    print(urlInTweet, urlInTweetIsNotEmpty, totalUrlInTweet)


    #To Make 

    #(\w)(\1{2,})

    #repeatLettersInTweet =  [t for t in tweet.split() if re.findall('(\w)(\1{2,})', t)]
    #repeatLettersInTweetIsNotEmpty = len(repeatLettersInTweet) != 0
    #totalRepeatLettersInTweet = len(repeatLettersInTweet)
    #print(repeatLettersInTweet, repeatLettersInTweetIsNotEmpty, totalRepeatLettersInTweet)
