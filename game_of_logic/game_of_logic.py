import argparse
from functools import reduce
import matplotlib.pyplot as plt
import numpy as np
import re
import urllib3


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', 
      help='id of ebook', 
      required=True, type=str)
    parser.add_argument('--validate',
      help='determine if url is valid',
      action='store_true')
    parser.add_argument('--num-results',
      help='how many results to plot', default=10, type=int)
    return parser.parse_args()


def get_ebook(id):
    """Retrieve ebook from Project Gutenberg in text format

    Args:
        id (int): book id from Project Gutenberg

    Returns:
        str: ebook text 
    """
    url = f'https://gutenberg.org/cache/epub/{id}/pg{id}.txt'
    resp = urllib3.request("GET", url)
    return str(resp.data)


def preprocess_ebook(ebook):    
    """Alterate the ebook to eliminate special characters

    Args:
        ebook (str): text version of the ebook

    Returns:
        list: text version of the ebook without special characters
    """
    pattern = r'\d+|\\r\\n|[-|="\';.&?!_,\\:@~`%$#*()+[\]{}<>]+'
    raw_text = ebook.lower().split('***')[2]
    raw_text = re.sub(pattern, ' ', raw_text).split()
    return raw_text


def get_interesting_words(raw_text):
    """Search for words that are more than five letters

    Args:
        raw_text (list): list of words in the text 

    Returns:
        list: list of words that are more than five letters
    """
    interesting_words = filter(lambda word: len(word) > 5, raw_text)
    return list(interesting_words)


def url_validate(id):
    """Validate url 

    Args:
        id (int): id of the ebook

    Returns:
        bool: True, if valid.  False, if otherwise.
    """
    url = f'https://gutenberg.org/cache/epub/{id}/pg{id}.txt'

    validation = urllib3.request("GET", url)

    if validation.status == 200:
        print("URL is valid")
        return True
    print("URL is invalid")
    return False


def generate_word_map(word_list):
    """ Creates a dictionary of word counts

    Args:
        word_list (list): list of interesting words in the ebook

    Returns:
        dictionary: Keys has the words and values has the count of the words.
    """
    word_map = {}
    for word in word_list:
        if word_map.get(word):
            word_map[word] += 1
        else:
            word_map[word] = 1
    return word_map


def amount_of_results(word_map, n):
    """Sort the dictionary by descending count

    Args:
        word_map (dictionary): dictionary of the words in the text
        n (int): top word count

    Returns:
        list: list of top n results 
    """
    result = sorted(word_map.items(), key=lambda x:x[1], reverse=True)
    return result[:n]


def plot_results(results):
    """A bar chart of the results

    Args:
        results (list): list of top n results
    """
    x = [result[0] for result in results]
    y = [result[1] for result in results]
    plt.bar(x, y, width=1, edgecolor='white', linewidth=0.7)
    plt.title('Most Frequent Words')
    plt.show()


def main():
    args = parse_arguments()
    if args.validate:
        url_validate(args.id)
        exit(0)
    ebook = get_ebook(args.id)
    raw_text = preprocess_ebook(ebook)
    interesting_words = get_interesting_words(raw_text)
    word_counts = generate_word_map(interesting_words)
    results = amount_of_results(word_counts, args.num_results)
    plot_results(results)

    
if __name__ == '__main__':
    main()