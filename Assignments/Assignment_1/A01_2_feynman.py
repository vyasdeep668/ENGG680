# Course: ENGG 680 Intro to Digital Engineering
# Assignment #: 1
# Topic: Text Analysis (2pt)
# Name: Deep Vyas
# UCID: 30139014

import re

ASSIGNMENT1_ROOT_DIR_PATH = 'C:/Users/vyasd/Desktop/ENGG680/Assignments/Assignment_1'
WORDS_TXT_FILE_PATH = ASSIGNMENT1_ROOT_DIR_PATH + '/words.txt'
BENCH_TXT_FILE_PATH = ASSIGNMENT1_ROOT_DIR_PATH + '/bench.txt'
FEYNMAN_TXT_FILE_PATH = ASSIGNMENT1_ROOT_DIR_PATH + '/feynman.txt'

# Read word.txt file and create list of words
file = open(FEYNMAN_TXT_FILE_PATH, "rt", encoding="utf8")
data = file.read()
words = data.split()
sentences = re.split("[.!?]", data)
words_len = len(words)
sentences_len = len(sentences) - 1


# Number of words in the text
print('Number of words in the text :', words_len)


# Number of sentences in the text
print('Number of sentences in the text :', sentences_len)


# The average number of words per sentence
print('The average number of words per sentence :', words_len/sentences_len)


# The average number of sentence parts (delineated by commas) per sentence
count = 0
for sentence in sentences:
    count = count + len(sentence.split(','))
print('The average number of sentence parts (delineated by commas) per sentence :', count/sentences_len)


# Number of personal pronouns, e.g. I, me, my, you, we
personal_pronouns = ["i", "you", "we", "he", "she", "it", "they"]
count = 0
for word in words:
    word = word.casefold()
    if word in personal_pronouns:
        count = count + 1
print('Number of personal pronouns, e.g. i, you, we, he, she, it, they : ', count)
