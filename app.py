import collections
import string
import re
import random

PATH = "./103.txt"
COM_PATH = "./common_words.txt"

def getTotalNumberOfWords():
    total_words = 0
    with open(PATH, 'r') as f:
        for line in f:
            clean_line = ''.join([c for c in line if c not in string.punctuation]).lower()
            for word in clean_line.split():
                total_words += 1
    print("Total Words: ")
    print(total_words)
    return total_words

def getTotalUniqueWords():
    s = set()
    with open(PATH, 'r') as f:
        for line in f:
            clean_line = ''.join([c for c in line if c not in string.punctuation]).lower()
            for word in clean_line.split():
                if word not in string.punctuation:
                    s.add(word.lower())
    print("Total Unique Words: ")
    print(len(s))
    return len(s)

def get20MostFrequentWords():
    m = collections.defaultdict(int)
    with open(PATH, 'r') as f:
        for line in f:
            clean_line = ''.join([c for c in line if c not in string.punctuation]).lower()
            for word in clean_line.split():
                if word not in string.punctuation:
                    m[word.lower()] += 1

    sorted_x = sorted(m.items(), key=lambda x: x[1], reverse=True)
    sorted_x = [x[0] for x in sorted_x[:20]]
    print("20 Most Frequent Words: ")
    print(sorted_x)
    return sorted_x

def get20MostInterestingFrequentWords():
    common_words = get_common_set(COM_PATH, 300)
    m = collections.defaultdict(int)
    with open(PATH, 'r') as f:
        for line in f:
            clean_line = ''.join([c for c in line if c not in string.punctuation]).lower()
            for word in clean_line.split():
                if word not in string.punctuation and word not in common_words:
                    m[word.lower()] += 1
    sorted_x = sorted(m.items(), key=lambda x: x[1], reverse=True)
    sorted_x = [x[0] for x in sorted_x[:20]]
    print("20 Most Frequent Words Exclude Common: ")
    print(sorted_x)
    return sorted_x

def get_common_set(path,limit):
    s = set()
    counter = 0
    with open(path, 'r') as f:
        for line in f:
            clean_line = ''.join([c for c in line if c not in string.punctuation]).lower()
            for word in clean_line.split():
                if word not in string.punctuation:
                    if counter < limit:
                        s.add(word)
                    else:
                        break
                    counter += 1
    return s

def get20LeastFrequentWords():
    m = collections.defaultdict(int)
    with open(PATH, 'r') as f:
        for line in f:
            clean_line = ''.join([c for c in line if c not in string.punctuation]).lower()
            for word in clean_line.split():
                if word not in string.punctuation:
                    m[word.lower()] += 1
        res = sorted(m.items(), key=lambda x: x[1], reverse=False)
        res = [x[0] for x in res[:20]]
    print("20 Least Frequent Words : ")
    print(res)

def getFrequencyOfWord(word):
    word_i = word.lower()
    res = []
    chapters = split_chapter()
    for x in range(0,len(chapters)):
        num_occur = 0
        current_chapter = chapters[x]
        current_chapter = current_chapter.split("\n")
        for line in current_chapter:
            clean_line = ''.join([c for c in line if c not in string.punctuation]).lower()
            for word in clean_line.split():
                if word not in string.punctuation:
                    if word_i == word:
                        num_occur += 1
        res.append(num_occur)
    print(res)


def getChapterQuoteAppears(quote):
    chapters = split_chapter()
    
    for x in range(0, len(chapters)):
        current_chapter = chapters[x].split("\n")
        current_string = ""
        for line in current_chapter:
            clean_line = ''.join([c for c in line if c not in string.punctuation]).lower()
            current_string += clean_line
        if ''.join([c for c in quote if c not in string.punctuation]).lower() in current_string:
            print("Chapter")
            print(x)
            return x
            
    return -1

def split_chapter():
    with open(PATH, 'r') as f:
        return re.split("Chapter", f.read())
            

getTotalNumberOfWords()
getTotalUniqueWords()
get20MostFrequentWords()
get20MostInterestingFrequentWords()
get20LeastFrequentWords()
getFrequencyOfWord("the")
getChapterQuoteAppears("fogg")
