import re
import random
import time
import codecs
import tweepy
import sys
import os

filename = "sentences.txt"

def getSentences(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    with codecs.open(filename, "r", encoding='utf-8', errors='ignore') as f:
        fulltext = f.read()
        sentencesSplit = re.split('[.?!]', fulltext)
        sentences = []
        for sentence in sentencesSplit:
            sentence = sentence.replace('\r', '').replace('\n', '').rstrip(' ')
            sentence = sentence.replace('\n', '')
            sentences += [sentence.split(' ')]
    f.close()
    return sentences

def getRandomSentence():
    sentences = getSentences(filename)
    word = random.choices(sentences)[0][0]
    randomSentence = word
    cont = True
    wordCount = 0
    while(cont):
        wordCount += 1
        if wordCount > 30:
            cont = False
        try:
            sentencesThatContainPreviousWord = []
            for sentence in sentences:
                if word in sentence:
                    sentencesThatContainPreviousWord += [sentence]
            randomSentenceThatContainsPreviousWord = random.choices(sentencesThatContainPreviousWord)[0]
            nextWordIndex = randomSentenceThatContainsPreviousWord.index(word)+1
            nextWord = randomSentenceThatContainsPreviousWord[nextWordIndex]
            randomSentence += " " + nextWord
            if nextWordIndex == len(randomSentenceThatContainsPreviousWord)-1:
                cont = False
            else:
                word = nextWord
        except:
            continue
    if randomSentence[-1:] != '.' and randomSentence[-1:] != '?' and randomSentence[-1:] != '!':
        randomSentence += '.'
    return randomSentence

def IsAllCaps():
    n = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    choice = random.choices(n)
    if choice[0] == 1:
        return True
    else:
        return False

def main():
    # TODO
    CONSUMER_KEY = 'Your Consumer Key'
    CONSUMER_SECRET = 'Your Consumer Secret'
    ACCESS_KEY = 'Your Access Key'
    ACCESS_SECRET = 'Your Access Secret'
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    n = [1, 2, 2]
    s = random.choices(n)
    oldSentence = ""
    sentence = ""
    while (True):
        try:
            for i in range(0, s[0]):
                if i == 0:
                    sentence = getRandomSentence()
                sentence += " " + getRandomSentence()
            if sentence[-1:] != '?' or sentence[-1:] != '!':
                sentence = sentence[:-1]
            allCaps = IsAllCaps()
            if allCaps:
                sentence = sentence.upper()
            api.update_status(sentence)
        except Exception as Error:
            api.update_status("Although there's a chance this may error as well, 
            + "this is where you can have your bot tweet when something goes wrong. 
            + "I recommend including your '@' so that you receive a notification.")
        time.sleep(7200)

if __name__ == "__main__":
    main()