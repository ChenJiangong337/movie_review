# Intro

Collect: Crawl lots of information related to movie reviews from douban.com based on scrapy framework, 4205 items in total  
Prepare: Extract short-reviews and scores from the data, replace the scores by 1(positive) and 0(negative)，segment the reviews, generate the vocabulary and parse text into token vectors using the bag-of-words document model  
Train: Based on naïve Bayes  
Test: Randomly generate train sets and test sets, then train and test them, repeat ten times and return every error rate and the mean accuracy 

# How to use

Based on python 3.6.5, scrapy 1.5.1

To crawl data from douban.com and save it:  
Execute the order in the same path as those codes:  
`scrapy crawl review -o XXX.csv(any filename you'd like)`  

To use the classifier:  
Operate the file: `movie_classifier.py`  
It will operate the classifier for 10 times and return every error rate and the mean accuracy. 
