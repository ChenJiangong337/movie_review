#   Filename: movie_classifier.py

import codecs
import csv
import jieba
import random
import nltk
import bayes

#读取从网站中爬取的影评
f = codecs.open('tutorial/review.csv','r',encoding='utf-8')
reader = csv.reader(f)

data = []
for item in reader:
    data.append(item)
documents = data[1:]
f.close()

def MakeWordsSet(words_file):
    words_set = set()                                            #创建set集合
    with codecs.open(words_file, 'r', encoding = 'utf-8') as f1:        #打开文件
        for line in f1.readlines():                                #一行一行读取
            word = line.strip()                                    #去回车
            words_set.add(word)                                   #有文本，则添加到words_set中
    words_set.add(' ')
    words_set.add('\n')
    return words_set                                             #返回处理结果
stopwords = MakeWordsSet('stopwords_cn.txt')

emotion = []
seg_review = []

for item in documents:
    #获取评分，即分类器标签
    score = int(item[4])
    if score >= 30:
        emotion.append(1)   #1为'好评'，0为'差评'
    else:
        emotion.append(0)
    #获取影评，使用结巴分词进行分词
    review = item[5]
    seg_list = jieba.cut(review)
    for string in seg_list:
        #去除数字、标点符号以及停用词
        if not string.isdigit() and string not in stopwords:
            seg_review.append(string)

#获取词汇表
all_words = nltk.FreqDist(w for w in seg_review)
word_features = [w for (w,_) in all_words.most_common(5000)]
print('The vocabulary has been created successfully!')

#对影评和评分进行整合，调整格式使之能够被分类器识别
featuresets = []
for i in range(len(emotion)):
               d = documents[i][5]
               c = emotion[i]
               featuresets.append((d,c))

sumRate = 0
for i in range(10):
    #打乱顺序确保每次结果均不同
    random.shuffle(featuresets)
    train_set, test_set = featuresets[int(0.1*len(emotion)):], featuresets[:int(0.1*len(emotion))]
    #训练分类器，使用分类器，并返回分类器错误分类的条目以及错误率
    errorItem,errorRate = bayes.classifier(train_set,test_set,word_features)
    sumRate += errorRate
meanRate = 1-sumRate/10
print('mean accuracy:{:.2%}'.format(meanRate))

