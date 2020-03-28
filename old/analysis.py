import json
from textblob import TextBlob

with open('twitter_data.txt') as f:
    contents = json.load(f)
    x = TextBlob(contents['text'])
    # y = contents['country_code']
    print(x)
    print(x.sentiment)
    

    
    