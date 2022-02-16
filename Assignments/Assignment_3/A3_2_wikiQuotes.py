# Course: ENGG 680 Intro to Digital Engineering
# Assignment #: 3
# Topic: WikiQuotes (3 pts)
# Name: Deep Vyas
# UCID: 30139014

import json
import pandas as pd

"""
TODO: 1- Read the json file quotes-100-en.json into a dictionary using the json module
"""
quotes_jason_pth = 'quotes-100-en.json'
quotes_jason_file = open(quotes_jason_pth, "rt", encoding='utf-8')
quotes_jason_dict = json.load(quotes_jason_file)


def search_quote(name, quote):
    """ 
        TODO:
        test1
        2- Write a function search_quotes that takes a string as argument,
           searches the keys in the quotes dictionary for items containing 
           the search string and prints the matching name (key) and quotes.
    """
    if name in quotes_jason_dict.keys():
        if quote in quotes_jason_dict[name]:
            print(name, ':', quote)
        else:
            print("quote not found!")
    else:
        print("name not found!")


def main():
    name = ["Albert Einstein", "Richard Feynman"]
    quote = ["The mass of a body is a measure of its energy content.",
             "PrinciplesAll mass is interaction."]
    search_quote(name[0], quote[0])
    search_quote(name[1], quote[1])
    """
        TODO:
        3- create a number of quotes list
        4- Combine quote keys and number of quotes into a DataFrame
        5- sort and reset index to get rank
    """
    df = pd.DataFrame({key: len(value) for key, value in quotes_jason_dict.items()}.items(), columns=['Name', 'Quotes Count'])
    df = df.sort_values(by='Quotes Count', ascending=False).reset_index(drop=True)
    print(df.loc[(df["Name"] == name[0]) | (df["Name"] == name[1])])


if __name__ == "__main__":
    main()
