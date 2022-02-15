# Course: ENGG 680 Intro to Digital Engineering
# Assignment #: 1
# Topic: Parsing industrial input file by using regular expression (2pt)
# Name: Deep Vyas
# UCID: 30139014

import re


ASSIGNMENT1_ROOT_DIR_PATH = 'C:/Users/vyasd/Desktop/ENGG680/Assignments/Assignment_1'
WORDS_TXT_FILE_PATH = ASSIGNMENT1_ROOT_DIR_PATH + '/words.txt'
BENCH_TXT_FILE_PATH = ASSIGNMENT1_ROOT_DIR_PATH + '/bench.txt'
FEYNMAN_TXT_FILE_PATH = ASSIGNMENT1_ROOT_DIR_PATH + '/feynman.txt'

# Read word.txt file and create list of words
file = open(BENCH_TXT_FILE_PATH, "rt")
data = file.read()
sentences = data.split(';')


# Set required sentences format
str_format = '^- inst[0-9][0-9][0-9][0-9]'  # - inst2015 NAND3X2 + PLACED ( 88000 78660 ) N ;

for sentence in sentences:
    sentence = sentence.strip()
    if bool(re.match(str_format, sentence)):
        print(sentence)
