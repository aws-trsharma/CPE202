"""
CPE 202: Project 4
Author: Tushar Sharma
"""
import os
import math
from hashtables import HashTableLinear, import_stopwords

class SearchEngine:
    """
    Attributes:
        directory (str): a directory name
        stopwords (Hashmap): a hashtable containing stopwords
        doc_length (Hashmap): hash table containing total number of words in document
    """
    def __init__(self, directory, stopwords):
        self.doc_length = HashTableLinear()
        self.term_freqs = HashTableLinear()
        self.stopwords = stopwords
        self.index_files(directory)

    def read_file(self, infile):
        """
        Helper Function to read files. Reads in all Files excluding stop words
        :param
            infile: (str): the path to a file
        :return:
            list: a list of str read from a file
        """
        out_list = []
        file = open(infile, 'r')
        for line in file:
            line = line.split(" ")
            for word in line:
                if '\n' in word:
                    word = word.replace('\n', '')
                if '.' in word:
                    word = word.replace('.', '')
                if '(' in word:
                    word = word.replace('(', '')
                if ')' in word:
                    word = word.replace(')', '')
                word = word.lower()
                if word not in self.stopwords:
                    out_list.append(word)
        return out_list


    def parse_words(self, lines):
        """
        splits strings into words
        Converts words to lower cases and removes new line chars
        :param
            lines: (list): a list of strings
        :return:
            list: a list of words
        """
        out_list = []
        for line in lines:
            line = line
            for word in line.split(" "):
                if '\n' in word:
                    word = word.replace('\n', '')
                if '.' in word:
                    word = word.replace('.', '')
                if '(' in word:
                    word = word.replace('(', '')
                if ')' in word:
                    word = word.replace(')', '')
                word = word.lower()
                if word not in self.stopwords:
                    out_list.append(word)
        return out_list

    def count_words(self, filename, words):
        """
        Count the number of words in the file and store frequency of each word in the
        term_freqs hashtable. The keys of the hashtable are the words and the hashtable contains
        a pointer to an inner hashtable that is  file names. The value of the hashtable is frequency of word
            filename: the file which contains the word
            words: contains the word
        :return:
            Hashtable which contains term_freqs
        """
        for word in words:

            if word not in self.term_freqs:
                inner_hash = HashTableLinear()
                count = self.count_freq(words, word, 0)
                inner_hash.put(filename, count)
                self.term_freqs.put(word, inner_hash)
            elif word in self.term_freqs:
                count = self.count_freq(words, word, 0)
                if self.term_freqs[word][filename] is not None:
                    self.term_freqs[word][filename] = count
                else:
                    self.term_freqs[word].put(filename, count)
        self.doc_length.put(filename, len(words))
        return self.term_freqs


    def count_freq(self, words, word, count):
        """
        Counts the frequency of the words and returns the count of that words specifically
        :param
            words: (list): a list of words
            word: the specific word to be counted
            count: the count of the frequency
        :return:
            count: the count of the frequency
        """
        for val in words:
            if word == val:
                count += 1
        return count

    def index_files(self, directory):
        """
        Indexes all text files in a given directory
        :param directory: The directory where all the files are stored
        :return: an inverted index
        """
        files = os.listdir(directory)
        for file in files:
            file = os.path.join(directory, file)
            if os.path.isfile(file) is True:
                check = os.path.splitext(file)
                if check[1] == ".txt":
                    self.count_words(file, self.read_file(file))

    def get_wf(self, tf):
        """
        Computes the weighted frequency
        :param
            tf (float): the term frequency
        :return
            wf (float): the weighted frequency
        """
        if tf > 0:
            wf = 1 + math.log(tf)
        else:
            wf = 0
        return wf

    def get_scores(self, terms):
        """
        creates a list of scores for each files in corpus
        :param
            terms: (list): a list of str
        :return:
            list: (list): a list of tuples, each containing the filename and its relevant corpus
        """
        scores = HashTableLinear()
        all_scores_list = []
        for term in terms:

            t = self.term_freqs[term]

            if term in self.term_freqs.key():
                if t is None:
                    continue
                for file in t.key():
                    if scores[file] is not None:
                        scores.put(file, scores[file] + self.get_wf(self.term_freqs[term][file]))
                    else:
                        scores.put(file, self.get_wf(self.term_freqs[term][file]))
        for infile in scores.key():
            scores[infile] /= self.doc_length[infile]

                #if scores[infile] == 0:
                #all_scores_list = []
            all_scores_list.append((infile, scores[infile]))

        return all_scores_list

    def rank(self, scores):
        """
        Ranks Files in the descending order of relevancy
        :param
            scores (list): a list of tuples: (filename, score)
        :return:
            a list of tuples sorted in descending order of relevancy
        """
        return sorted(scores, key = lambda x:x[1], reverse=True)

    def search(self, query):
        """
        search for the query times in the file
        :param
            query (str): a query input
        :return:
            list: list of files in descending order or relevancy
        """
        check_col = HashTableLinear()
        #print(query)
        #query = query.split(" ")
        new_que = self.parse_words(query)
        if len(new_que) is None:
            return None
        fin = []
        for cur in new_que:
            if check_col.contains(cur) is False:
                check_col.put(cur, cur)
                fin.append(cur)

        tot = 0
        scores = self.get_scores(fin)
        test = self.rank(scores)
        for i in test:
            print(i[0])
            tot += i[1]

        return tot

ht = HashTableLinear()
stop_words = import_stopwords("stop_words.txt", ht)

#print(stop_words)
se = SearchEngine("docs", stop_words)

#words = se.read_file("data_structure.txt")
#words1 = se.read_file("hash_table.txt")
#se.count_words("data_structure.txt", words)
#print(se.count_words("hash_table.txt", words1))
#print(se.term_freqs)
#print(se.doc_length)
#vw = se.get_scores(['goldstein'])
print(se.get_scores(['goldstein']))
print(se.search(['hash', 'table']))
#print(se.get_scores(['science']))

#print(se.search('adt'))










