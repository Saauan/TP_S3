'''
   Compute the entropy on files.

   @author Tayebi Ajwad, Coignion Tristan
'''

import sys
from math import log2


#TODO Q1 & Q2

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
    
    Text, Occu = stream.read(), {}
    try:
        for elt in Text:
            if bytes([elt]) in Occu.keys():
                Occu[bytes([elt])] +=1
            else:
                Occu[bytes([elt])] = 1
                
    except TypeError:
        for elt in Text:
            if elt in Occu.keys():
                Occu[elt] +=1
            else:
                Occu[elt] = 1
    return Occu


def entropy(filename): 
    '''
    Computes the entropy of the file called `filename`.

    :param filename: Input file name.
    :type filename: str
    :return: A tuple whose first element is an integer: the number of bytes read
    and the second element is a float: the entropy of the file's content
    :rtype: tuple
    '''
    with open(filename, 'rb') as infile :
        counters = symbol_occurrences(infile)
        total_sum, nb_bytes = 0, sum(counters.values())
        for cpt in counters:
            total_sum += counters[cpt] * log2(counters[cpt])
        total_sum = log2(nb_bytes) - (total_sum/nb_bytes)
        reduction = (100*total_sum) / 8 # Q6
    return (nb_bytes, total_sum, 100-reduction)



#Q5
#Ici, étant donné que c'est un codage binaire, l'encadrement de notre fichier est représenté de la sorte :
# entropy(X) <= (n Σ i=0) pi*ci < entropy(X) + 1

#Q7 à faire




def usage():
    print("Usage: {:s} <filename>".format(sys.argv[0]))
    print("\t<filename>: filename for which we want to compute the entropy.\n")
    exit(1)

def main():
    if len(sys.argv) != 2:
        usage()
    (nb_bytes, entro,reduc) = entropy(sys.argv[1])
    print("{:d} bytes read.".format(nb_bytes))
    print("Entropy = {:f} bits per byte.".format(entro))
    print("An optimal coding would reduce this file size by {:f}%".format(reduc))
    
if __name__ == '__main__':
    main()

    import doctest
    doctest.testmod(verbose=False, optionflags=doctest.ELLIPSIS)