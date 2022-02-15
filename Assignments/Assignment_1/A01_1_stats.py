# Course: ENGG 680 Intro to Digital Engineering
# Assignment #: 1
# Topic: Word List Statistics (2pt)
# Name: Deep Vyas
# UCID: 30139014


ASSIGNMENT1_ROOT_DIR_PATH = 'C:/Users/vyasd/Desktop/ENGG680/Assignments/Assignment_1'
WORDS_TXT_FILE_PATH = ASSIGNMENT1_ROOT_DIR_PATH + '/words.txt'
BENCH_TXT_FILE_PATH = ASSIGNMENT1_ROOT_DIR_PATH + '/bench.txt'
FEYNMAN_TXT_FILE_PATH = ASSIGNMENT1_ROOT_DIR_PATH + '/feynman.txt'

# Read word.txt file and create list of words
file = open(WORDS_TXT_FILE_PATH, "rt")
data = file.read()
words = data.split()

# Number of words in the list
print('Number of words in the list :', len(words))

# Average word length
count = 0
for word in words:
    count = count + len(word)
avg = count/len(words)
print('Average word length :', avg)

# Maximum word length
max_len = len(max(words, key=len))
print('Maximum word length :', max_len)


# Number of words that use all vowels 'aeiou'
count = 0
for word in words:
    if (word.find('a') != -1) and (word.find('e') != -1) and (word.find('i') != -1) and \
       (word.find('o') != -1) and (word.find('u') != -1):
        count = count + 1

print('Number of words that use all vowels \'aeiou\': ', count)


# Number of abecedarian words
count = 0
for word in words:
    if word == ''.join(sorted(word)):
        count = count + 1

print('Number of abecedarian words: ', count)
