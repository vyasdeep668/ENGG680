# Course: ENGG 680 Intro to Digital Engineering
# Assignment #: 2
# Topic: Analyze Book with Histogram Class (2.5pt)
# Name: Deep Vyas
# UCID: 30139014

import random
import collections
import itertools


class Histogram(dict):
    """A histogram to count frequencies of elements.

    Inherits dict which will hold element-frequency pairs
    Elements are provided by Lists (iterables)
    """

    def __init__(self, l=None):
        """Constructor: provide elements in a list or iterable"""
        if l is not None:
            self.count(l)

    def __str__(self):
        """ returns a string representation of each element-frequency pair"""
        # TODO: Add your code
        # For each entry in histogram, this should append to return string:
        # {value} count of {element}\n
        # the last pair should not have the trailing ‘\n’
        string = ""
        for key, value in self.items():
            string = string + "({} count of {})\n".format(value, key)

        return string[:-1]

    def __sub__(self, other):
        """Subtraction: Returns a dictionary with all keys that appear in self but not other.

        other: Histogram() object
        """
        # TODO: Add your code
        return {key: value for key, value in sorted(self.items(), key=lambda x: x[0]) if key not in other.keys()}

    def most_common(self, n=None):
        """Returns n most common (most frequent) elements in histogram

        if n=None, all are returned

        returns: List of Tuples, each Tuple is a element-frequency pair
        """
        # TODO: Add your code
        # Follow analyze_book1 but make sure you add (element, frequency)
        return [(key, value) for key, value in dict(itertools.islice(self.items(), n if not None else len(self.items()))).items()]

    def count(self, l):
        """Adds items in list l to the histogram"""
        # TODO: Add your code
        [self.__setitem__(item[0], item[1]) for item in sorted(dict(collections.Counter(l)).items(), key=lambda x: (x[1], x[0]), reverse=True)]
        # self[item[0]] = item[1]

    def total_elements(self):
        """Returns the total of the frequencies in a histogram."""
        # TODO: Add your code
        return sum(self.values())

    def different_elements(self):
        """Returns the number of different words in a histogram."""
        # TODO: Add your code
        return len(self)

    def random_element(self):
        """Chooses a random word from a histogram.

        The probability of each word is proportional to its frequency.
        returns: string a single words
        """
        # TODO: Add your code
        return str(random.choices(list(self.keys()), weights=[element / self.total_elements() for element in
                                                              list(self.values())], k=1))


def test(title, produced, expected):
    print("*** Test {}".format(title))
    if produced == expected:
        print("   PASS")
    else:
        print("   FAIL")
        print("   expected {}".format(expected))
        print("   produced {}".format(produced))


if __name__ == '__main__':
    a = [1, 2, 3, 1, 1, 2]
    b = 'Hello Calgary! What a great day. Calgary is a great city.'
    c = b.split()

    hist_int = Histogram()
    hist_int.count(a)

    hist_char = Histogram(b)

    hist_word = Histogram(c)

    test("Initialize with count()",
         str(hist_int),
         "(3 count of 1)\n(2 count of 2)\n(1 count of 3)")

    test("int hist most_common all",
         str(hist_int.most_common()),
         "[(1, 3), (2, 2), (3, 1)]")

    test("char hist most_common n=3",
         str(hist_char.most_common(n=3)),
         "[('a', 10), (' ', 10), ('y', 4)]")

    test("word hist most_common n=5",
         str(hist_word.most_common(n=5)),
         "[('great', 2), ('a', 2), ('is', 1), ('day.', 1), ('city.', 1)]")
