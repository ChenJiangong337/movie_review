# Intro

Collect: Crawl lots of information related to movie reviews from douban.com based on scrapy framework, 23407 items in total  
Prepare: Extract short-reviews and scores from the data, replace the scores by 1(positive) and 0(negative)，segment the reviews, generate the vocabulary and parse text into token vectors using the bag-of-words document model  
Train: Based on naïve Bayes  
Test: Randomly generate train sets and test sets, then train and test them, repeat ten times and return every error rate and the mean accuracy 

# How to use

Based on python 3.6.5, scrapy 1.5.1  
Make sure that those modules are in your PC: jieba, numpy, nltk, codecs  
Although there is an embeded bayes classifier in the nltk module, I have created an independent one so that I could utilize it flexiblely  

To crawl data from douban.com and save it, you need execute those orders in the path 'tutorial':  
First, get the movie ids:  
`scrapy crawl movieid -o id.csv`  
Then, get the reviews:  
`scrapy crawl review -o review.csv`  

To use the classifier:  
Operate the file: `movie_classifier.py`  
