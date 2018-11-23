#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
   Compute the entropy on files.

   @author FIL - IEEA - Univ. Lille 1 (oct 2010, août 2015)
'''

import sys
from math import log2
from math import floor

# IMPORTS A COMPLETER

###### Question 1 ##########

##la valeur de l'entropie maximal est 11

###### Question 2 ##########

# h(f) = -(255 ∑ i=0) pi * log2(pi)
#      = -(255 ∑ i=0) ni/N * log2(ni/N)
#      = -(255 ∑ i=0) ni/N * (log2(ni)-log2(N))
#      = -(255 ∑ i=0) ni/N * log2(ni) + (255 ∑ i=0) ni/N * log2(N)
#      = log2(N) (255 ∑ i=0) ni/N * log2(ni)
#      = log2(N) (255 ∑ i=0) ni * log2(ni) / N

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
    
    occurrence = dict()
    byte=stream.read(1)
    read=True 
    while read :
        if byte == b'' or byte == '':
            read = False
        else:
            if byte in occurrence.keys():
                occurrence[byte]+=1
            else:
                occurrence[byte]=1
        byte = stream.read(1)
    return occurrence
        


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
    for i in counters:
        total_sum= total_sum + (counters[i]*log2(counters[i]))
        nb_bytes+= counters[i]
    total_sum=  log2(nb_bytes)-(total_sum/ nb_bytes)
    infile.close()
    reduction=((total_sum*nb_bytes)/(nb_bytes*8))*100
    return ( nb_bytes , total_sum,100-reduction)

#### Question 4 ####

##$ python3 entropy.py cigale.txt 
##624 bytes read.
##Entropy = 4.507422 bits per byte.
##
##$ python3 entropy.py codage.bmp 
##378054 bytes read.
##Entropy = 4.447328 bits per byte.
##
##$ python3 entropy.py sonnet18.txt
##626 bytes read.
##Entropy = 4.397370 bits per byte.

 
#### Question 5 ####

##H(S) * nb_bytes <= |nc| * nb_bytes <= H(S)+1 * nb_bytes





if __name__ == '__main__':
    import doctest
    doctest.testmod()
    

def usage():
    print("Usage: {:s} <filename>".format(sys.argv[0]))
    print("\t<filename>: filename for which we want to compute the entropy.\n")
    exit(1)

def main():
    if len(sys.argv) != 2:
        usage()
    (nb_bytes, entro, reduction ) = entropy(sys.argv[1])
    print("{:d} bytes read.".format(nb_bytes))
    print("Entropy = {:f} bits per byte.".format(entro))
    print('An optimal coding would reduce this file size by',reduction,'%')
    
if __name__ == '__main__':
    main()

    
