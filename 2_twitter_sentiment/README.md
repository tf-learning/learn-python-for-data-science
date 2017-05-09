# [Twitter Sentiment Analysis - Learn Python for Data Science 2](https://www.youtube.com/watch?v=o_OZdbCzHUA)

tokenization of each tweet by word creating a bag of words
the bag of words and read it from a lexicon 

```
virtualevn -p python3 venv
pip install tweepy
pip install textblob
```

Download the nltk files
```
python
>>> import nltk
>>> nltk.download()
```

Try out TextBlob. Sentiment polarity is based on a range of -1 to 1.
```
python
>>> from textblob import TextBlob
>>> wiki = TextBlob("Craig is great at Machine Learning")
>>> wiki.tags
[('Craig', 'NNP'), ('is', 'VBZ'), ('great', 'JJ'), ('at', 'IN'), ('Machine', 'NNP'), ('Learning', 'NNP')]
>>> wiki.words
WordList(['Craig', 'is', 'great', 'at', 'Machine', 'Learning'])
>>> wiki.sentiment
Sentiment(polarity=0.8, subjectivity=0.75)
>>> wiki.sentiment.polarity
0.8
```

# Environment variables

```
source environ
```

sets the variables for:
```
export TWITTER_CONSUMER_KEY
export TWITTER_CONSUMER_SECRET
export TWITTER_ACCESS_TOKEN
export TWITTER_ACCESS_TOKEN_SECRET
```
