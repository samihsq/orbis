from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "1017906040128430080-IJL8j2GmrCoA4w5E3RaW75CIawEoVr"
access_token_secret = "4xeEhJ6PAlETej6t2XjlCkY9b2wYLbcSibgepdGkUTPBf"
consumer_key = "btwz4EP3m8x4f721NNVgLKCKS"
consumer_secret = "8j710jSIzOwXcDAyA5nFrJq7nOHCQAJcBlrUYNOa6VD2o5yK9r"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['happy', 'sad', 'bad', 'terrible', 'good', 'amazing'])
