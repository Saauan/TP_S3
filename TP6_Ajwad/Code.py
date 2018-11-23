######################
#####Question 2#######
######################

## Utilisation de la methode code
##>>> my_coding.code('a')
##'010'
##
##>>> my_coding.code('b')
##'100'
##
##>>> my_coding.code('c')
##'110'


######################
#####Question 3#######
######################

##Utilisation de la methode decode

##>>> my_coding.decode('010')
##'a'
##

##>>> my_coding.decode('100')
##'b'
##
##>>> my_coding.decode('110')
##'c'

###### Question 4 ######

##Lorsque l'on code un cractere non defini on obtient :
##
##    raise Not_codable_symbol()
##coding.Not_codable_symbol


##### Question 5 #######

##Lorsque l'on decode un caractere non defini on obitent :
##
##    raise Undecodable_word()
##coding.Undecodable_word


##### Question 6 ######

from coding import *
source_alphabet =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']

code1 = [ "00000", "00001", "00010", "00011", "00100", "00101", "00110", "00111", "01000", "01001", "01010", "01011", "01100", "01101", "01110", "01111", "10000", "10001", "10010", "10011", "10100", "10101", "10110", "10111", "11000", "11001", "11111" ]
code2 =  [".-/", "-.../", "-.-./", "-../", "./", "..-./", "--./", "..../", "../", ".---/", "-.-/", ".-../", "--/", "-./", "---/", ".--./", "--.-/", ".-./", ".../", "-/", "..-/", "...-/", ".--/", "-..-/", "-.--/", "--../", "---./"]
code3 = ["1010", "0010011", "01001", "01110", "110", "0111100", "0111110", "0010010", "1000", "011111110", "011111111001", "0001", "00101", "1001", "0000", "01000", "0111101", "0101", "1011", "0110", "0011", "001000", "011111111000", "01111110", "0111111111", "01111111101", "111"]

coding1 = create(source_alphabet, code1)
coding2 = create(source_alphabet, code2)
coding3 = create(source_alphabet, code3)


############ Question 7##############
##
##Mot = 'C EST MON ANNIVERSAIRE'
##
##Codage de mot
##
##>>> for i in mot:
##    print(my_conding3.code(i),end="")
##    
## 01001111110101101101110010100001001111101010011001100000100011001011011101010000101110
##>>> for i in mot:
##    print(my_conding2.code(i),end="")
##    
##-.-./---././.../-/---./--/---/-./---./.-/-./-./../...-/./.-./.../.-/../.-././
##>>> for i in mot:
##    print(my_conding1.code(i),end="")
##    
## 00010111110010010010100111111101100011100110111111000000110101101010001010100100100011001000000010001000100100

## Si on decode :

##>>> my_conding1.decode("10011")
##'T'
##>>> my_conding2.decode("-..-/")
##'X'
##>>> my_conding3.decode("1010")
##'A'


##### Question 8 #####


def code_word(mot,codage):
    """
    code a word with the provided coding
    
    :param mot: the word to be coded
    :param codage: the coding to use for coding the word
    :type mot: str
    :type codage: coding
    :return: word coded with codage
    :rtype: str
    :CU: Symbols in the word are in the source alphabet of the coding
    
    exemple:
    
    >>> code_word('', coding1)
    ''
    >>> code_word('ABCD', coding1)
    '00000000010001000011'
    >>> code_word(' ZA', coding1)
    '111111100100000'
    
    """
    
    mot1=""
    for i in mot:
        mot1=mot1+codage.code(i)
    return mot1
        
######## QUestion 9 ########

##On obitent les bonne choses
##
##>>> code_word("CODAGE",code1)
##'000100111000011000000011000100'
##>>> code_word("CODAGE",code2)
##'-.-./---/-../.-/--././'
##>>> code_word("CODAGE",code3)
##'0100100000111010100111110110'



##### Question 10 / 11 ######

def decode_fixed_length_word(mot,coding):
    """
    Decode a word using a fixed-length coding
    
    :param mot: the codeword to be decoded
    :param coding:  the coding to use for decoding the codeword
    :type mot: str
    :type coding: coding
    :return: he result of decoding codeword with coding
    :rtype:str
    :CU: The codeword was obtained from the coding my_coding
    
    Examples:

    >>> decode_fixed_length_word('', coding1)
    ''
    >>> decode_fixed_length_word('111111100100000', coding1)
    ' ZA'
    >>> decode_fixed_length_word(code_word(''.join(source_alphabet), coding1), coding1)
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
    >>> decode_fixed_length_word('11111110010000', coding1)
    Traceback (most recent call last):
    ...
    coding.Undecodable_word: decode_fixed_length_word: undecodable word
    >>> decode_fixed_length_word('1   22', coding1)
    Traceback (most recent call last):
    ...
    coding.Undecodable_word: decode_fixed_length_word: undecodable word
    
    """
    l= len(coding.code('A'))
    if len(mot)%l != 0:
        raise Undecodable_word ("decode_fixed_length_word: undecodable word")
    else:
        res=""
        cpt=0
        for i in range(l,len(mot)+1,l):
            try:
                lettre=coding.decode(mot[cpt:i])
            except:
                raise Undecodable_word 
            cpt=i
            res=res+lettre
        return res


######### Question 13 ##########
##Le mot à décoder est :
##    'LA PHILANTHROPIE DE L OUVRIER CHARPENTIER'
################################


######### Question 14 / 15 ###########

def decode_comma_word(mot,virgule,codage):
    """

    Code a word with the provided comma coding
    
    :param mot: the word to be coded
    :param virgule: the symbol used as a separator
    :param codage: the coding to use for coding the word
    :return: word decoded with codage
    :type mot: str
    :type virgule: str
    :type codage: coding
    :rtype: str
    
    Exemple:
    
    >>> decode_comma_word('', '/', coding2)
    ''
    >>> decode_comma_word(code_word(''.join(source_alphabet), coding2), '/', coding2)
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
    >>> decode_comma_word('-.../-.-', '/', coding2)
    Traceback (most recent call last):
    ...
    coding.Undecodable_word: decode_comma_word: comma not found, cannot decode the word
    
    """
    
    res=''
    while mot!="":
        pos=mot.find(virgule)
        try:
            lettre=codage.decode(mot[0:pos+1])
        except:
            raise Undecodable_word ("decode_comma_word: comma not found, cannot decode the word")
        mot=mot[pos+1:]
        res=res+lettre
    return res

######### Question 16 ############
##
##Le mot à decoder est :
##    'POUR LA FRANCE D EN BAS DES NOUILLES ENCORE'
##################################


def decode_prefix_letter(word, my_coding):
    '''
    Decodes the first letter of the word, assuming a prefix coding was used.

    :param word: A word that was coded using `coding`
    :type word: str
    :param my_coding: The coding used for (de)coding
    :type my_coding: coding.Coding
    :return: a tuple whose elements are: 1) the symbol associated with the\
    first decodable prefix 2) the length of the first decodable prefix
    :rtype: tuple
    :CU: `word` was coded using `my_coding`
    :Examples:

    >>> decode_prefix_letter("0010010", coding3)
    ('H', 7)
    >>> decode_prefix_letter("00100101000", coding3)
    ('H', 7)
    >>> decode_prefix_letter("00", coding3)
    Traceback (most recent call last):
    ...
    coding.Undecodable_word: decode_prefix_letter: no decodable prefix
    '''
    word_length = len(word)
    for i in range(1,word_length+1):
        try:
            prefix = my_coding.decode(word[:i])
            return (prefix, i)
        except:
            pass
    raise Undecodable_word("decode_prefix_letter: no decodable prefix")


############ Question 17 / 18 ###########################

def decode_prefixe_word(mot,codage):
    """
    decode a word with a prefix coding
    
    :param mot: the word to be decoded
    :param codage:the prefix coding that was used for coding the word
    :type mot: str
    :type codage: coding
    :return: word decoded with codage
    :rtype: str
    :CU: The word was coded using the coding my_coding
    
    Exemples:
    
    >>> decode_prefixe_word("0010010", coding3)
    'H'
    >>> decode_prefixe_word("00100101000", coding3)
    'HI'
    >>> decode_prefixe_word("00", coding3)   
    Traceback (most recent call last):
    ...
    coding.Undecodable_word
    >>> decode_prefixe_word(code_word(''.join(source_alphabet), coding3), coding3)
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
    
    """
    res=""
    while mot != "":
        try:
            lettre=decode_prefix_letter(mot,codage)
        except:
            raise Undecodable_word
        res=res+lettre[0]
        mot=mot[lettre[1]:]
    return res


##################### Question 19 #####################

###  Le mot à decoder est 'THALES EST TOUJOURS A FAIRE'

#######################################################

##################Question 20 ########################


def integer_to_binary_str(integer):
    """
    Get a binary representation of an integer
    
    :param integer: the integer to be converted in binary
    :type integer: int
    :return: Return the binary representation (as a string) of integer
    :rtype: str
    :CU: integer >=0
    
    Example:
    
    >>> integer_to_binary_str(1)
    '1'
    >>> integer_to_binary_str(2)
    '10'
    >>> integer_to_binary_str(53)
    '110101'

    
    """
    
    assert integer >= 0 , 'Integer have to be positive'
    mot=bin(integer)
    return mot[2:]

def binary_str_to_integer(bin_str):
    """
    Inverse function of conversions.integer_to_binary_str()
    
    :param bin_str: the input binary string
    :type bin_str: str
    :return: The integer whose binary representation is bin_str
    :rtype: int
    :CU: bin_str is a binary string (containing only 0s or 1s).
    
    Examples:
    
    >>> binary_str_to_integer("0")
    0
    >>> binary_str_to_integer("110101")
    53
    >>> binary_str_to_integer("10000000")
    128
    
    """
    return int(bin_str, 2)
    
    
    
def binary_to_bytes(binary):
    '''
    Get a list of bytes corresponding to a binary string.

    :param binary: A binary string representing one or several bytes
    :type binary: str
    :return: A list of bytes. We assume that the binary string is encoded\
    in big endian
    :rtype: list
    :CU: `binary` is a binary string whose length is a multiple of 8.
    :Examples:

    >>> binary_to_bytes('11010110')
    [214]
    >>> binary_to_bytes('110101101101011111011000')
    [214, 215, 216]
    '''
    assert(len(binary) % 8 == 0), "The string must have a multiple of 8 bits"

    return [ binary_str_to_integer(binary[i:i+8]) for i in range(0, len(binary), 8) ]

def byte_to_binary(byte):
    '''
    Get the binary representation of a byte.

    :param byte: The byte to be conerted to binary
    :type byte: int
    :return: The binary representation, as a string of length 8, of `byte`.
    :rtype: str
    :CU: byte >= 0 and byte < 256
    :Examples:

    >>> byte_to_binary(1)
    '00000001'
    >>> byte_to_binary(255)
    '11111111'
    '''
    assert(byte >= 0 and byte <= 255), "byte_to_binary: this is not a byte"
    binaire = integer_to_binary_str(byte)
    return '0' * (8 - len(binaire)) + binaire


###### Question 21 ######

def write_bits(stream, bits):
    """
    Write bits (a number multiple of 8) in a writable stream.
    
    :param stream:  a steam opened in write and binary modes
    :param bits:  a string made of binary characters
    :type stream: stream
    :type bits : str
    :return: the bits that have not been written yet to the stream.
    :rtype: str
    :CU: None
    
    Example:
    
    >>> # Next line creates a temporary file for tests
    >>> import tempfile; r=tempfile.NamedTemporaryFile()
    >>> write_bits(r, '11011111')
    ''
    >>> write_bits(r, '110')
    '110'
    >>> write_bits(r, '11011111000000010110')
    '0110'
    >>> r.seek(0) # Go back at the start of the file
    0
    >>> list(r.read()) # Read the three bytes that should have been written to the file
    [223, 223, 1]
    >>> write_bits(tempfile.NamedTemporaryFile(mode='w'), '11011111000000010110')
    Traceback (most recent call last):
    ...
    AssertionError: The stream must be opened in write and binary modes ('wb')
    
    """
    
    assert 'b' in stream.mode and stream.writable() == True , "The stream must be opened in write and binary modes ('wb')"
    Longueur = len(bits)
    if Longueur<=7:
        return bits
    else:
        stream.write(bytes(binary_to_bytes(bits[:8])))
        return write_bits(stream,bits[8:])

##### Question 22 #####
    
def complete_byte(bits):
    """
    Completes a byte.
    
    :param bits: a binary string
    :type bits: str
    :return:  A binary string of 8 bits which completes the string bits. The completion adds a 1 followed by as many zeroes as necessary to reach 8 bits.
    :rtype: str
    :CU: len(bits)<8
    
    Example:
    
    >>> complete_byte('01')
    '01100000'
    >>> complete_byte('0100001')
    '01000011'
    >>> complete_byte('')
    '10000000'
    >>> complete_byte('00000001')
    Traceback (most recent call last):
    ...
    AssertionError: I cannot complete a completed byte!
    
    """
    assert len(bits) < 8 , 'I cannot complete a completed byte!'
    bits=bits+'1'
    length=len(bits)
    while len(bits) < 8 :
        bits=bits+'0'
    return bits
    
   
#### Question 23 ######   
    
def read_bits(stream):
    """
    Get the first 8 bits from the input stream.
        
    :param stream: The input stream which was opened in read and binary modes.
    :type stream: stream
    :return: A binary string made of 8 bits (or an empty string)
    :r type: stre
    :CU: The stream was opened in read and binary modes.
        
    Examples:
        
    >>> # Create a temporary file
    >>> import tempfile; r=tempfile.NamedTemporaryFile(); 
    >>> write_bits(r, '1101111100000001') # Write data into the file
    ''
    >>> r.seek(0) # Go back at the start of the file
    0
    >>> read_bits(r) # Read the first 8 bits
    '11011111'
    >>> read_bits(r) # Read the following 8 bits
    '00000001'
    >>> read_bits(r) # The end of the file is reached
    ''
            
    """
        
    assert 'b' in stream.mode, "The stream must be opened in binary modes ('b')"
    T = stream.read(1)
    try:
        return byte_to_binary(T[0])
    except:
        return ''
    
    
###### Question 24 ######


def uncomplete_byte(bits):
    """
    The reverse function of complete_byte.
    
    :param bits: a string of 8 bits
    :type bits: str
    :return: A binary string of length < 8 for which the completion was removed (from the last 1-bit to the end)
    :rtype: str
    :CU: 	len(bits) == 8 and the byte must have at least one 1-bit.
    
    Example:
    
    >>> uncomplete_byte('01100000')
    '01'
    >>> uncomplete_byte('01000011')
    '0100001'
    >>> uncomplete_byte('10000000')
    ''
    >>> uncomplete_byte('0000000')
    Traceback (most recent call last):
    ...
    AssertionError: I can only uncomplete a byte
    
    """
    assert '1' in bits and len(bits) == 8, 'I can only uncomplete a byte'
    mot=bits
    if mot=='10000000':
        return ''
    for i in range(7,0,-1):
        if bits[i] =='1':
            return mot[:i]

###### Question 25 ######

def remove_completion(bits):
    """
    Remove the completion bits from the end of a binary string.
    
    :param bits:a binary string of length >= 8 (which was already completed)
    :type bits: str
    :return: Return the binary string where the completion has been removed at the end (please note that the completion is done only on the last byte).
    :rtype: str
    :CU: len(bits)>=8
    
    Examples:
    
    >>> remove_completion('1010101010000000')
    '10101010'
    >>> remove_completion('1010101001100000')
    '1010101001'
    
    
    """
    assert len(bits)>=8 , "Bits need to be a str with a minimum length 8"
    for i in range(len(bits)-1,-1,-1):
        if bits[i]=='1':
            return bits[0:i]
    


def flush_binary_string(binary, stream):
    '''
    Flush a binary string by writing as many bytes as possible in the output
    stream.

    :param binary: A binary string
    :type binary: str
    :param stream: An output stream
    :return: the bits that could not be written in the output stream (the\
    length of the returned string is necessarily < 8).
    :Examples:

    >>> import tempfile; r=tempfile.NamedTemporaryFile()
    >>> flush_binary_string('01000001', r)
    ''
    >>> r.seek(0);
    0
    >>> r.read().decode()
    'A'
    '''
    while len(binary) >= 8:
        binary = write_bits(stream, binary)
    return binary

def write_binary_string_in_file(binary, file):
    '''
    Write the binary string in the file (the string is written 8 bits per 8
    bits in the file).
    As the binary string can have any length, the last byte will be completed
    so that all the content could be written to the file.

    :param binary: a binary string
    :type binary: str
    :param file: The filename of the file where the binary string will be\
    written
    :type file: str
    :Examples:

    >>> import tempfile; r=tempfile.NamedTemporaryFile()
    >>> write_binary_string_in_file('01000001010', r.name)
    >>> r.seek(0);
    0
    >>> r.read().decode()
    'AP'
    '''
    out_file = open(file, 'wb')
    binary = flush_binary_string(binary, out_file)
    write_bits(out_file, complete_byte(binary))
    out_file.close()

def read_file(file):
    '''
    Read the data in the file and returns a binary string corresponding to
    that data.

    :param file: the filanem of the file to read.
    :type file: str
    :return: The binary string of the data that was stored in the file. The\
    completion will be removed from the binary string.
    :rtype: str
    :Examples:

    >>> import tempfile; r=tempfile.NamedTemporaryFile()
    >>> write_binary_string_in_file('01000001010', r.name)
    >>> r.seek(0);
    0
    >>> read_file(r.name)
    '01000001010'
    '''
    in_file = open(file, 'rb')
    bits = ''
    binaire = read_bits(in_file)
    while binaire != '':
        bits += binaire
        binaire = read_bits(in_file)
    in_file.close
    if len(bits) > 0:
        bits = remove_completion(bits)
    return bits
    
        
        
###### Question 26 ##########

##Le fichier comptes 15 octets
## La difference est du au b devant le chaine de caractere d'ou un bits de plus sois 113 bits  sois 15 octets

###### Question 27########
## C'est la même chaine de caractére 

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    