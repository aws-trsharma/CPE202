"""
CPE 202: Project 4
Author: Tushar Sharma
"""
"""
Runs the Search Engine Class
"""
import sys
import os
from SearchEngineClass import *
from hashtables import HashTableLinear

def main():
    """
    Takes in a directory name and creates a search engine class
    :return:
        Relevant documents and a list of file names with relevenacy
    """
    directory = sys.argv[1]
    ht = HashTableLinear()
    stop_words = import_stopwords('stop_words.txt', ht)
    search_e = SearchEngine(directory, stop_words)
    no_end = False
    while no_end is False:
        cur = input("Enter Search:")
        input1 = cur.split()
        if input1[0][0] == 'q':
            break
        if input1[0][0] == 's':
            remove_2 = input1[0][2:]
            input1[0] = remove_2
            print(search_e.search(input1[1:]))




if __name__ == '__main__':
    main()