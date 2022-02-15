# Course: ENGG 680 Intro to Digital Engineering
# Assignment #: 2
# Topic: Analyze Book with Histogram Class (2.5pt)
# Name: Deep Vyas
# UCID: 30139014

"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import string

import Histogram as hg


def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header

    returns: Histogram object - map from each word to the number of times it appears.
    """
    word_list = []
    fp = open(filename)

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        if line.startswith('*** END OF THIS'):
            break

        process_line(line, word_list)

    # TODO: Create Histogram object from word_list
    hist = hg.Histogram(word_list)

    return hist


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """

    for line in fp:
        if line.startswith('*** START OF THIS'):
            break


def process_line(line, word_list):
    """Cleans the string in line and adds the words to word_list.

    Cleaning steps:
    1. replace '-' with ' '
    2. strip punctuation and whitespace
    3. convert to lowercase

    Modifies word_list.

    line: string
    word_list: List containing individual words as elements
    """

    # replace hyphens with spaces before splitting
    line = line.replace('-', ' ')
    strippables = string.punctuation + string.whitespace

    for word in line.split():
        # remove punctuation and convert to lowercase
        word = word.strip(strippables)
        word = word.lower()

        # TODO: update the list
        word_list.append(word)


def main():
    hist = process_file('feynman.txt', skip_header=False)
    print('Total number of words:', hist.total_elements())
    print('Number of different words:', hist.different_elements())

    t = hist.most_common()
    print('The most common words are:')
    for freq, word in t[0:20]:
        print(word, '\t', freq)

    words = process_file('words.txt', skip_header=False)

    diff = hist - words  # Subtract two Histogram objects

    print("The words in the book that aren't in the word list are:")
    for word in diff.keys():
        print(word, end=' ')

    print("\n\nHere are some random words from the book:")
    for i in range(100):
        print(hist.random_element(), end=' ')
    print('')


if __name__ == '__main__':
    main()
