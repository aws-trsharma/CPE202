"""Huffman Coding
CPE202

Author:
    Tushar Sharma
"""
from HuffmanNode import HuffmanNode
from min_pq import MinPQ

def cnt_freq(filename):
    """
    Opens a text file and returns a list of 256 integers and counts frequency of occurences
    """
    list_of_freq = [0] * 256
    file = open(filename, 'r')
    for line in file:
        for char in line:
            list_of_freq[ord(char)] += 1
    return list_of_freq


def create_huff_tree(list_of_freqs):
    """
    returns the root node of a Huffman Tree
    """
    arr = []
    min_pq = MinPQ()
    for i in range(len(list_of_freqs)):
        if list_of_freqs[i] != 0:
            arr.append(HuffmanNode(list_of_freqs[i], chr(i)))
    min_pq.heapify(arr)
    print(min_pq)
    while min_pq.num_items > 1:
        min1 = min_pq.del_min()
        min2 = min_pq.del_min()
        if ord(min1.char) > ord(min2.char) and min1.freq == min2.freq:
            new_huff = HuffmanNode(min1.freq + min2.freq, min(min1.char, min2.char), min2, min1)
        else:
            new_huff = HuffmanNode(min1.freq + min2.freq, min(min1.char, min2.char), min1, min2)
        min_pq.insert(new_huff)
    return min_pq.arr[0]


def create_code(root_node, arr_code = [],  code1 = ''):
    """returns a Python list of 256 strings representing the code
    Return an array of size 256 whose idex corresponds to ascii code of a letter.
    """
    if len(arr_code) == 0:
        arr_code =[None] * 256
    if root_node is None:
        return
    if root_node.left is None and root_node.right is None:
        arr_code[ord(root_node.char)] = code1
    create_code(root_node.left, arr_code, code1 + '0')
    create_code(root_node.right, arr_code, code1 + '1')
    return arr_code

def huffman_encode(in_file, out_file):
    """encodes in_file and writes the it to out_file
    This function calls cnt_freq, create_huff_tree, and create_code functions.
    """
    arr_code = cnt_freq(in_file)
    root_node = create_huff_tree(arr_code)
    arr = create_code(root_node)
    out_file = open(out_file, 'w')
    in_file = open(in_file, 'r')
    string = ''
    for line in in_file:
        for char in line:
            out_file.write(arr[ord(char)])
    out_file.write(string)
    out_file.close()
    return out_file
#val = cnt_freq('test1.txt')
#print(create_huff_tree(val))
#print(huffman_encode('test2.txt', 'encodetest2.txt'))


