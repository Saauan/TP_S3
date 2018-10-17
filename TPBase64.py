#Q2
" Si il ne possède aucun '=', cela signifie que codé en ASCII, le nombre de bits est un multiple de 6."
" Si il possède un seul '=', cela signifie qu'il a fallut rajouter 2 bits nuls pour completer un dernier sextet."
" Si il possède deux '=', cela signifie qu'il a fallut rajouter 4 bits nuls pour completer un dernier sextet."


#Q3
BASE64_SYMBOLS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                        'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                                        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                                        'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
                                        'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                                        'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                                        'w', 'x', 'y', 'z', '0', '1', '2', '3',
                                        '4', '5', '6', '7', '8', '9', '+', '/']

print(BASE64_SYMBOLS[2],BASE64_SYMBOLS[40],BASE64_SYMBOLS[34],BASE64_SYMBOLS[39])


#Q4

def many_bytes_to_int(some_bytes):
    """
    Returns an integer consisting of the representation of all the bytes in some_bytes

    :param:	some_bytes – A bytes object containing several (>= 0) bytes
    :type: bytes
    :return: An integer whose binary representation is the binary representation of the bytes in some_bytes.
    The most significant byte in the returned integer is the first byte in some_bytes
    :rtype: int
    :CU: None
    
    Examples:	
    >>> many_bytes_to_int(bytes([253, 12, 71]))
    16583751
    >>> many_bytes_to_int(bytes([23, 12, 71]))
    1510471
    >>> many_bytes_to_int(bytes([16]))
    16
    >>> many_bytes_to_int([])
    0
    >>> many_bytes_to_int(bytes([129, 126]))
    33150
    """
    if some_bytes == [] :
        return 0
    elif len(some_bytes) == 1:
        return some_bytes[0]
    else:
        return some_bytes[0] << 2**(len(some_bytes) + 1) | many_bytes_to_int(some_bytes[1:])



#Q5
# Remainder : 1 byte = 8 bits
def int_to_sextets(integer, nb_bytes):
    """
    Convert an integer made from nb_bytes bytes to at most 4 sextets

    :param:	integer (int) – The integer to convert
                nb_bytes (int) – Number of bytes that were used to represent the integer integer
    :return: A list of at most 4 values, each representing a sextet, converted from the initial integer.
                The first sextet from the list is made from the 6 most significant bits of the integer,
                    the following sextet is made from the following six bits and so on.
    :rtype:	list
    :CU: nb_bytes <= 3 and integer < 2**(8 * nb_bytes)

    Examples:	
    >>> int_to_sextets(many_bytes_to_int(bytes([253, 12, 71])), 3)
    [63, 16, 49, 7]
    >>> int_to_sextets(many_bytes_to_int(bytes([23, 12, 71])), 3)
    [5, 48, 49, 7]
    >>> int_to_sextets(16, 1)
    [4, 0]
    >>> int_to_sextets(0, 0)
    []
    >>> int_to_sextets(0, 1)
    [0, 0]
    """
    if (integer == 0 and nb_bytes == 0):
        return []
    elif (integer==0 and nb_bytes != 0) or (integer != 0 and nb_bytes == 0):
        return [0,0]
    else:
        pass
    

#Q6
def bytes_to_symbol(data):
    """
    Takes (at most) three bytes of data in input and returns the corresponding base64 symbols.

    :param:	data – A list of at most three bytes
    :return:	Four base64 symbols (or ‘=’) corresponding to the data given in input
    :rtype:	str
    :CU:	len(data) <= 3
    
    Examples:	
    >>> bytes_to_symbols([5])
    'BQ=='
    >>> bytes_to_symbols([4, 163])
    'BKM='
    >>> bytes_to_symbols([28, 89, 101])
    'HFll'
    >>> bytes_to_symbols([])
    ''
    """
    assert len(data) > 3, "Your data length causes a problem, has to be at most equals to 3"
    
    if data == []:
        return ''
    
    sextets, symbol = int_to_sextets(many_bytes_to_int(data), len(data)), ""
    for k in sextets:
        symbol += BASE64_SYMBOLS[k]
        
    while len(symbol) < 4:
        symbol += '='
        
    return symbol