'''
   Compute the entropy on files.

   @author FIL - IEEA - Univ. Lille 1 (oct 2010, août 2015)
'''

import sys

# IMPORTS A COMPLETER

def symbol_occurrences(stream):
    '''
    Read the stream and count the occurrences of each symbol in the stream
    
    :param stream: a stream opened (in read mode and (possibly) in binary mode)
    :return: A dictionary whose keys are symbols and the associated values are\
    the corresponding number of occurrences
    :rtype: dict
    :Examples:
    
    >>> from io import StringIO # StringIO is used to have stream examples based on strings.
    >>> from io import BytesIO # BytesIO is used to have stream examples based on bytes.
    >>> symbol_occurrences(StringIO("ababcaba")) == {'c': 1, 'b': 3, 'a': 4}
    True
    >>> symbol_occurrences(BytesIO(b"ababcaba")) == {b'c': 1, b'b': 3, b'a': 4}
    True
    >>> symbol_occurrences(StringIO('aaaa')) == {'a': 4}
    True
    >>> symbol_occurrences(StringIO(''))
    {}
    >>> symbol_occurrences(StringIO('abcd')) == {'a': 1, 'b': 1, 'c': 1, 'd': 1}
    True
    >>> symbol_occurrences(BytesIO(b'abcd')) == {b'a': 1, b'b': 1, b'c': 1, b'd': 1}
    True
    '''

    # A COMPLETER


def entropy(filename): 
    '''
    Computes the entropy of the file called `filename`.

    :param filename: Input file name.
    :type filename: str
    :return: A tuple whose first element is an integer: the number of bytes read\
    and the second element is a float: the entropy of the file's content
    :rtype: tuple
    '''

    infile = open(filename, 'rb')
    # Dictionary that will store the number of occurrences of each byte.
    counters = symbol_occurrences(infile)
    
    # Calcul de l'entropie à partir des effectifs des octets.
    total_sum = 0
    nb_bytes = 0
    # A COMPLETER

    infile.close()

    return # A COMPLETER

def usage():
    print("Usage: {:s} <filename>".format(sys.argv[0]))
    print("\t<filename>: filename for which we want to compute the entropy.\n")
    exit(1)

def main():
    if len(sys.argv) != 2:
        usage()
    (nb_bytes, entro) = entropy(sys.argv[1])
    print("{:d} bytes read.".format(nb_bytes))
    print("Entropy = {:f} bits per byte.".format(entro))
    
if __name__ == '__main__':
    main()
