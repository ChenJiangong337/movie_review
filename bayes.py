'''
基于词袋模型的朴素贝叶斯分类器
'''
from numpy import *

                 
def createVocabList(dataSet):
    vocabSet = set([])  #create empty set
    for document in dataSet:
        vocabSet = vocabSet | set(document) #union of the two sets
    return list(vocabSet)


def trainNB0(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    p0Num = ones(numWords); p1Num = ones(numWords)      #change to ones() 
    p0Denom = 2.0; p1Denom = 2.0                        #change to 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num/p1Denom)        #change to log()
    p0Vect = log(p0Num/p0Denom)        #change to log()
    return p0Vect,p1Vect,pAbusive

def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)    #element-wise mult
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else: 
        return 0
    
def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec


def classifier(train_set,test_set,vocabList):
    trainMat=[]; trainClasses=[]
    for docIndex in train_set:
        trainMat.append(bagOfWords2VecMN(vocabList, docIndex[0]))
        trainClasses.append(docIndex[1])
    p0V,p1V,pSpam = trainNB0(array(trainMat),array(trainClasses))
    errorCount = 0
    errorItem = []
    for docIndex in test_set:        #classify the remaining items
        wordVector = bagOfWords2VecMN(vocabList, docIndex[0])
        if classifyNB(array(wordVector),p0V,p1V,pSpam) != docIndex[1]:
            errorCount += 1
            errorItem.append(docIndex)
    errorRate=float(errorCount)/len(test_set)
    print('errorRate:{:.2%}'.format(errorRate))
    return errorItem,errorRate
