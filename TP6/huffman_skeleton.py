'''
Implantation de l'algorithme de Huffman

@author FIL - IEEA - Univ. Lille (août 2015)
'''

import doctest
import operator
from huffman_tree import HuffmanTree
import coding
import struct
from TP5Coding import flush_binary_string, write_bits, read_file

def create_forest(occurrences):
    '''
    Create the initial list of Huffman trees based on the dictionary of
    symbols given in parameter.
    
    :param occurrences: Number of occurrences of each symbol.
    :type occurrences: dict
    :return: A list sorted in ascending order on the number of occurrences\
    and on the symbols of Huffman trees of all symbols provided in\
    `occurrences`.
    :Examples: 

    >>> create_forest({'a': 4, 'c': 2, 'b': 1})
    [|b:1|, |c:2|, |a:4|]
    >>> create_forest({'e': 1, 'f': 1, 'g': 1, 'h': 1, 'a':2})
    [|e:1|, |f:1|, |g:1|, |h:1|, |a:2|]
    '''
    sorted_occs = sorted(occurrences.items(), key=lambda item: (item[1], item[0]))
    forest = [HuffmanTree(leaf[0], leaf[1]) for leaf in sorted_occs]
    return forest

def pop_least_element(list1, list2):
    '''
    Get and remove the lowest element from two lists sorted in ascending order.

    :param list1: First list sorted in ascending order
    :type list1: list
    :param list2: Second list sorted in ascending order
    :type list2: list
    :return: The lowest element among the two lists
    :UC: The two lists are sorted in ascending order and there is at least\
    one element among the two lists.
    :Examples:

    >>> pop_least_element([1], [2])
    1
    >>> pop_least_element([2], [1])
    1
    >>> pop_least_element([], [1])
    1
    >>> pop_least_element( [1], [])
    1
    '''
    assert(len(list1) + len(list2) >= 1)
    if len(list1) == 0:
        return list2.pop(0)
    if len(list2) == 0:
        return list1.pop(0)
    if list2[0] < list1[0]:
        return list2.pop(0)
    return list1.pop(0)

def create_huffman_tree(occurrences):
    '''
    Return a Huffman tree of the symbols given in `occurrences`.
    
    :param occurrences: Number of occurrences of each symbol.
    :type occurrences: dict
    :return: Return a single Huffman tree (obtained with Huffman algorithm)\
    of the symbols in `occurrences`.
    :rtype: huffman_tree.HuffmanTre
    :Examples:
    
    >>> create_huffman_tree({'a': 4, 'b': 1, 'c': 2})
    |bca:7|_<|bc:3|_<|b:1|, |c:2|>, |a:4|>
    >>> create_huffman_tree({'a': 1, 'b': 1, 'c': 2})
    |cab:4|_<|c:2|, |ab:2|_<|a:1|, |b:1|>>
    '''
    symbol_list = create_forest(occurrences)
    tree_list = []

    while len(tree_list) + len(symbol_list) != 1:
        (elem1, elem2) = (pop_least_element(symbol_list, tree_list),\
                          pop_least_element(symbol_list, tree_list))
        new_tree = HuffmanTree(left = elem1, right=elem2)
        tree_list.append(new_tree)

    if len(tree_list) == 1:
        return tree_list[0]
    return symbol_list[0]

def get_coding_from_tree(tree, code=''):
    '''
    Get the codes associated to the symbols.

    :param tree: A HuffmanTree
    :type tree: huffman_tree.HuffmanTree
    :param code: (optional parameter) the path that was followed to access the\
    current root of the tree
    :return: a list of tuples. Each tuple is made of a symbol and a code.\
    The order of the tuples in the list does not matter
    :rtype: list
    :Examples:

    >>> c=get_coding_from_tree(create_huffman_tree({'a': 4, 'b': 1, 'c': 2}))
    >>> len(c)
    3
    >>> c.count(('a', '1')) == 1
    True
    >>> c.count(('b', '00')) == 1
    True
    >>> c.count(('c', '01')) == 1
    True
    '''
    if tree.isLeaf():
        return [(tree.symbol, code)]
    return get_coding_from_tree(tree.left, code + '0') \
        + get_coding_from_tree(tree.right, code + '1')
    
def huffman_coding(tree):
    '''
    Creates a Huffman coding from a Huffman tree.

    :param tree: A Huffman tree
    :type tree: huffman_tree.HuffmanTree
    :return: A Huffman coding based on the Huffman tree given in parameter
    :rtype: coding.Coding
    :Examples:

    >>> c = huffman_coding(create_huffman_tree({'a': 4, 'b': 1, 'c': 2}))
    >>> c.code('a') + ' ' + c.code('b') + ' ' + c.code('c')
    '1 00 01'
    >>> c = huffman_coding(create_huffman_tree({'a': 1, 'b': 2, 'c': 3, 'd': 5}))
    >>> c.code('a') + ' ' + c.code('b') + ' ' + c.code('c') + ' '\
    + c.code('d')
    '110 111 10 0'
    '''
    result = get_coding_from_tree(tree, '')
    alphabet = list(map(lambda i: i[0], result))
    codes = list(map(lambda i: i[1], result))
    return coding.create(alphabet, codes)

def write_occurrences(occurrences, filename):
    '''
    Write the symbol occurrences in the given file
    
    :param occurrences: The dictionary of symbol occurrences
    :type occurrences: dict
    :param filename: The filename where the occurrences must be written.
    :type filename: str
    '''
    
    stream = open(filename, 'wb')

    # A COMPLETER

    stream.close()

def read_occurrences(filename):
    '''
    Read the symbol occurrences from the given file.

    :param filename: The filename where the occurrences must be read.
    :type filename: str
    :return: A dictionary of the symbol occurrences
    :rtype: dict
    :Examples:

    >>> import tempfile; temp = tempfile.NamedTemporaryFile()
    >>> d = {b'c': 1, b'b': 3, b'a': 4}
    >>> write_occurrences(d, temp.name)
    >>> read_occurrences(temp.name) == d
    True
    >>> d = {b'e': 1, b'f': 1, b'g': 1, b'h': 1, b'a':2}
    >>> write_occurrences(d, temp.name)
    >>> read_occurrences(temp.name) == d
    True
    '''

    # A COMPLETER

    
def huffman_encode(filename, out_filename):
    '''
    Encode a file using Huffman algorithm and writes the result to 
    an other file.
    
    Two files will be created. One called `out_filename` containing
    a Huffman encoding of the input file. Another one called
    `out_filename`+".code" which will contain the occurrences of each 
    symbol.

    :param filename: The filename of the file to be encoded.
    :type filename: str
    :param out_filename: The filename of the file where the resulting\
    encoding will be stored.
    :type out_filename: str
    '''
    stream = open(filename, 'rb')
    # Calcul du nombre d'occurrences

    # Création du codage de Huffman

    # Ecriture du fichier stockant le dictionnaire d'occurrences

    # Mise de la tête de lecture au début du fichier pour le reparcourir
    
    # Parcours du fichier et encodage des symboles lus

    stream.close()

def prefix_tree_decoding(bits, tree):
    '''
    Return the decoding of the binary string given in parameter
    using the Huffman tree `tree`.
    
    :param bits: a binary string (only made of 0s and 1s)
    :type bits: str
    :param tree: a Huffman tree
    :type tree: huffman_tree.HuffmanTree
    :return: Return the concatenation of symbols represented by the binary string.\
    The binary string is decoded using the Huffman tree.
    :rtype: bytes
    :UC: The binary string must end in a leaf.
    :Examples:

    >>> tree = create_huffman_tree({b'a': 1, b'b': 2, b'c': 3, b'd': 5})
    >>> prefix_tree_decoding('111110100111111110', tree)
    b'bacdbba'
    '''

    # A COMPLETER
    
def huffman_decode(filename, out_filename):
    '''
    Decode a file encoded with a Huffman encoding.

    :param filename: the file name of the Huffman encoded file
    :type filename: str
    :param out_filename: the file name where the decoding will be stored
    :type out_filename: str
    '''
    occurrences = read_occurrences(filename+".code")
    arbre = create_huffman_tree(occurrences)

    bits = tpcodings.read_file(filename)
    out_file = open(out_filename, 'wb')
    out_file.write(prefix_tree_decoding(bits, arbre))
    out_file.close()
