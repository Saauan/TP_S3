from coding import *
import stack1 as stack

#Q1
src_alphabet, code = ['a','b','c'], ['010','100','110']
my_coding = create(src_alphabet, code)




#Q2 & #Q3
print(my_coding.code(src_alphabet[0]), my_coding.code(src_alphabet[1]), my_coding.code(src_alphabet[2]))
print(my_coding.decode(code[0]), my_coding.decode(code[1]), my_coding.decode(code[2]),"\n\n")




#Q4 & #Q5
#print(my_coding.code('d')) -> on a l'apparition d'une erreur "coding.Not_codable_symbol"
#print(my_coding.decode('001')) -> on a l'apparition d'une erreur "coding.Undecodable_word"





#Q6
import string
SRC_ALPHABET = list(string.ascii_uppercase) + [" "]

code1 = ["00000","00001","00010","00011","00100","00101","00110","00111","01000",
         "01001","01010","01011","01100","01101","01110","01111","10000","10001",
         "10010","10011","10100","10101","10110","10111","11000","11001","11111"]

code2 = [".-/", "-.../", "-.-./", "-../", "./", "..-./", "--./", "..../ ", "../",
         ".---/", "-.-/", ".-../", "--/", "-./", "---/", ".--./", "--.-/", ".-./",
         ".../", "-/", "..-/", "...-/", ".--/", "-..-/", "-.--/", "--../", "---./"]

code3 = ["1010","0010011","01001","01110","110","0111100","0111110",
         "0010010","1000","011111110","011111111001","0001","00101",
         "1001","0000","01000","0111101","0101","1011","0110","0011",
         "001000","011111111000","01111110","0111111111","01111111101","111"]


coding1, coding2, coding3 = create(SRC_ALPHABET, code1), create(SRC_ALPHABET, code2), create(SRC_ALPHABET, code3)




#Q7
print(coding1.code('C'), coding1.code('O'), coding1.code('I'), coding1.code('N'))
print(coding2.code('S'), coding2.code('O'), coding2.code('S'))
print(coding3.decode("0010011"), coding3.decode("0101"), coding3.decode("1010"), coding3.decode("001000"), coding3.decode("0000"), "\n")




#Q8 & 9
def code_word(word, coding):
    """
    Returns your initial word in the chosen coding
    
    :param: word (str) - the word you want to code in UPPERCASE
            coding (Coding) - the Coding you want for your word
    :return: cword (str) - the word coded
    :CU: None
    
    Examples:
    >>> code_word('CODAGE', coding1)
    '000100111000011000000011000100'
    >>> code_word('CODAGE', coding2)
    '-.-./---/-../.-/--././'
    >>> code_word('CODAGE', coding3)
    '0100100000111010100111110110'
    """
    cword = ""
    for carac in word:
        cword += coding.code(carac)
    
    return cword




#Q10
# On remarque la présence d'un attribut alphabet() qui renvoie l'alphabet du code,
# de ce fait, pour obtenir la longueur, on calcule simplement len(coding.code(coding.alphabet()[0]))




#Q11 & Q12
def decode_fixed_length(cword, coding):
    """
    Returns your initial coded word decoded in SRC_ALPHABET
    
    :param: cword (str) - the word you want to decode in UPPERCASE
            coding (Coding) - the Coding of your word (fixed length)
    :return: dword (str) - the word decoded
    :CU: None
    
    Examples:
    >>> decode_fixed_length("00010011100100001101",coding1)
    'COIN'
    >>> decode_fixed_length(code_word('CODAGE', coding1), coding1)
    'CODAGE'
    """
    if cword == "":
        return cword
    else:
        l = len(coding.code(coding.alphabet()[0]))
        try:
            return coding.decode(cword[0:l]) + decode_fixed_length(cword[l:],coding)
        except TypeError:
            raise Undecodable_word("decode_fixed_length_word: undecodable word")




#Q13
print(decode_fixed_length("0101100000111110111100111010000101100000011011001100111100010111001111010000010011111000110010011111010111111101110101001010110001010000010010001111110001000111000001000101111001000110110011010000010010001", coding1), "\n")




#Q14
print('"test".find("Ceci est un test") renvoie', "test".find("Ceci est un test"))
print('tandis que "Ceci est un test".find("test") renvoie', "Ceci est un test".find("test"), "\n")

print('Ensuite, "xXx".find("Le film XxX est sympathique") renvoie', "xXx".find("Le film xXx est sympathique"))
print('mais "Le film XxX est sympathique".find("xXx") renverra aussi', "Le film XxX est sympathique".find("xXx"), "\n")




#Q15 & #Q16
def decode_comma_word(cword, comma, coding):
    """
    Decode a word with the provided comma coding
    
    :param: cword (str) - the word you want to decode
            comma (str) - the character used as the comma
            coding (Coding) - the Coding of your word
    :return: decoded word (str)
    :CU: len(comma) == 1
    
    Examples:
    >>> decode_comma_word('', '/', coding2)
    ''
    >>> decode_comma_word('.-/-.../-.-./','/',coding2)
    'ABC'
    >>> decode_comma_word('-.../-.-', '/', coding2)
    Traceback (most recent call last):
    ...
    coding.Undecodable_word
    """
    if cword == "":
        return cword
    else:
        cword = cword.split(comma)
        for k in range(len(cword) - 1):
            cword[k] += comma
        try:
            return coding.decode(cword[0]) + decode_comma_word(''.join(cword[1:]),comma,coding)
        except TypeError:
            raise Undecodable_word("decode_comma_word: comma not found, cannot decode the word")




#Q16
print(decode_comma_word(".--./---/..-/.-./---./.-../.-/---./..-./.-./.-/-./-.-././---./-../---././-./---./-.../.-/.../---./-.././.../---./-./---/..-/../.-../.-.././.../---././-./-.-./---/.-././", "/", coding2) + "\n")




#Q17
def decode_prefix_letter(cword, coding):
    """
    Decodes the first letter of the word, assuming a prefix coding was used.
    
    :param: cword (str) - a word that was coded using ‘ Coding ‘
            coding (Coding) - The coding used for the coding
    :return: (tuple) whose elements are :
                1) the symbol associated with the first decodable prefix
                2) the length of the first decodable prefix
    :CU: ‘ cword ‘ was coded using ‘ coding ‘
    
    Examples:
    >>> decode_prefix_letter("0010010", coding3)
    ('H', 7)
    >>> decode_prefix_letter("00100101000", coding3)
    ('H', 7)
    >>> decode_prefix_letter("00", coding3)
    Traceback (most recent call last):
    ...
    coding.Undecodable_word: decode_prefix_letter : no decodable prefix
    """
    for i in range (1, len(cword) + 1):
        try :
            prefix = coding.decode(cword[:i])
            return (prefix,i)
        except :
            pass
    raise Undecodable_word("decode_prefix_letter : no decodable prefix")




#Q18
def decode_prefix_word(cword, coding, dword = ""):
    """
    Decode a prefix word
    
    :param: cword (str) - the word you want to decode coded using the coding given
            coding (Coding) - the Coding of your word
    :return: decoded word (str)
    :CU: None
    
    Examples:
    >>> decode_prefix_word("0010010", coding3)
    'H'
    >>> decode_prefix_word("00100101000", coding3)
    'HI'
    """
    if cword == "":
        return dword
    for x in cword:
        try:
            (letter, index) = decode_prefix_letter(cword, coding)
            return decode_prefix_word(cword[index:], coding, dword + letter)
        except:
            raise Undecodable_word("decode_prefix_letter : no decodable prefix")




#Q19
print(decode_prefix_word("0110001001010100001110101111111010110110111011000000011011111110000000110101101111110101110111100101010000101110", coding3) + "\n")
        



#Q20
def integer_to_binary_str(integer):
    """
    Gives the representation of integer in binary
    
    :param: integer (int) - the integer you want to convert
    :return: bin_str (str) - the binary representation of integer
    :CU: integer >= 0
    
    Examples:
    >>> integer_to_binary_str(1)
    '1'
    >>> integer_to_binary_str(2)
    '10'
    >>> integer_to_binary_str(53)
    '110101'
    """
    bin_str = "" ; st = stack.Stack()
    if integer == 0:
        return '0'
    while integer != 0:
        a = integer%2 ; integer = integer//2
        st.push(str(a))
    while not st.is_empty():
        bin_str += st.pop()
    return bin_str




def binary_str_to_integer(bin_str):
    """
    Inverse function of integer_to_binary_str()
    
    :param: bin_str (str) - the binary string you want to convert back into integer
    :return: integer (int) - the integer whose representation is bin_str
    :CU: bin_str only composed of 0s and 1s 
    
    Examples:
    >>> binary_str_to_integer("0")
    0
    >>> binary_str_to_integer("110101")
    53
    >>> binary_str_to_integer("10000000")
    128
    """
    integer = 0 ; st = stack.Stack()
    while bin_str != "":
        a = int(bin_str[0]) * 2**(len(bin_str)-1)
        bin_str = bin_str[1:]
        st.push(a)
    while not st.is_empty():
        integer += st.pop()
    return integer




def binary_to_bytes(binary):
    """
    Get a list of bytes corresponding to a binary string.
    
    :param: binary (str) - A binary string representing one or several bytes
    :return: (list) of bytes -  We assume that the binary string is encoded in big endian
    :CU: ‘ binary ‘ is a binary string whose length is a multiple of 8.
    
    Examples:
    >>> binary_to_bytes("11010110")
    [214]
    >>> binary_to_bytes ("110101101101011111011000")
    [214, 215, 216]
    """
    assert (len(binary)%8 == 0), "The string must have a multiple of 8 bits"
    return [binary_str_to_integer(binary[i:i+8]) for i in range (0, len(binary), 8)]




def byte_to_binary(byte):
    """
    Get the binary representation of a byte.
    
    :param: byte (int) - The byte to be converted to binary
    :return: (str) of the binary representation of byte as a string of length 8, of ‘ byte ‘.
    :CU: 0 <= byte < 256
    
    Examples:
    >>> binary_to_bytes("11010110")
    [214]
    >>> binary_to_bytes ("110101101101011111011000")
    [214, 215, 216]
    """
    assert (byte >= 0 and byte <= 255), "byte_to_binary : this is not a byte"
    return '0' * (8 - len(integer_to_binary_str(byte))) + integer_to_binary_str(byte)




#Q21
def write_bits(stream, bits):
    """
    Write bits (a number multiple of 8) in a writable stream.

    :param: stream - an opened stream in write and binary modes
            bits (str) - a string made of binary characters
    :action:	Writes all the possible bits to the stream.
             We recall that bits can only be written byte per byte (8 bits per 8 bits).
    :return:	The bits that have not been written yet to the stream.

    Examples:	
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
    """
    if len(bits) < 8:
        return bits
    else:
        stream.write(bits[0:8])
        return write_bits(stream, bits[8:])
    


#f = open('file.txt', 'wb')
#f.write(bytes([65,66]))
#f.close()
    # => permet d'écrire dans un fichier les caractères ayant pour représentation binaire 65 & 66 en ASCII, soit AB




#Q22
def complete_byte(bits):
    """
    Completes a byte.

    :param: bits (str) - a binary string
    :return:	A binary string (str) of 8 bits which completes the string bits.
             The completion adds a 1 followed by as many zeroes as necessary to reach 8 bits.

    Examples:	
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
    assert len(bits) < 8, "I cannot complete a completed byte!"
    
    bits += "1"
    while len(bits) < 8 :
        bits += "0"
    return bits




#Q23
def read_bits(stream):
    """
    Get the first 8 bits from the input stream.

    :param: stream – The input stream which was opened in read and binary modes.
    :return:	A binary string (str) made of 8 bits (or an empty string)
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
    text = stream.read()
    try:
        return text[0:8]
        text = text[8:]
    except:
        return ''



#Q24
def uncomplete_byte(bits):
    """
    The reverse function of complete_byte.

    :param: bits (str) - a string of 8 bits
    :return:	A binary string (str) of length < 8 for which the completion was removed
             (from the last 1-bit to the end).
    :CU: len(bits) == 8 & must contain at least one 1-bit

    Examples:	
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
    assert len(bits) == 8 and "1" in bits, "I can only uncomplete a byte"
    return bits[0:bits.rfind("1")]




#Q25
def remove_completion(bits):
    """
    Remove the completion bits from the end of a binary string.

    :param: bits (str) - a binary string of length >= 8 (which was already completed)
    :return:	Return the binary string (str) where the completion has been removed at the end
             (please note that the completion is done only on the last byte).
    :CU: len(bits) >= 8

    Examples:	
    >>> remove_completion('1010101010000000')
    '10101010'
    >>> remove_completion('1010101001100000')
    '1010101001'
    """
    l = len(bits)
    assert l >= 8
    return bits[0:l-8] + uncomplete_byte(bits[l-8:])




#Q26
def flush_binary_string(binary, stream):
    """
    Flush a binary string by writing as many bytes as possible in the output
    stream.
    
    :param: binary (str) - A binary string
            stream - an output stream
    :return: the bits that could not be written in the output stream
             (the length of the returned string is necessarily < 8).
    
    Examples :
    >>> import tempfile ; r = tempfile.NamedTemporaryFile()
    >>> flush_binary_string('01000001',r)
    ''
    >>> r.seek(0);
    0
    >>> r.read().decode()
    'A'
    """
    while len(binary) >= 8:
        binary = write_bits(stream, binary)
    return binary




def write_binary_string_in_file(binary, file):
    """
    Write the binary string in the file (the string is written 8 bits per 8 bits in the file).
    As the binary string can have any length , the last byte will be completed so
    that all the content could be written to the file.
    
    :param: binary (str) - A binary string
            file (str) - the filename of the file where the binary string will be written
    
    Examples :
    >>> import tempfile ; r = tempfile . NamedTemporaryFile ()
    >>> write_binary_string_in_file('01000001010', r.name)
    >>> r.seek(0);
    0
    >>> r.read().decode()
    'AP'
    """
    out_file = open(file,'wb')
    binary = flush_binary_string(binary, out_file)
    write_bits(out_file, complete_byte(binary))
    out_file.close()




def read_file(file):
    """
    Read the data in the file and returns a binary string corresponding to that data.
    
    :param: file (str) - the filename of the file to read
    :return: The binary string (str) of the data that was stored in the file.
             The completion will be removed from the binary string.
    
    Examples :
    >>> import tempfile ; r = tempfile . NamedTemporaryFile ()
    >>> write_binary_string_in_file('01000001010',r.name )
    >>> r.seek(0);
    0
    >>> read_file (r.name)
    '01000001010'
    """
    in_file = open(file, 'rb')
    bits = ''
    binaire = read_bits(in_file)
    while binaire != "":
        bits += binaire
        binaire = read_bits(in_file)
    in_file.close
    if len(bits) > 0:
        bits = remove_completion(bits)
    return bits




#write_binary_string_in_file("0110001001010100001110101111111010110110111011000000011011111110000000110101101111110101110111100101010000101110", "mot3.data")



#Q27
#read_file("mot3.data")


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False, optionflags=doctest.ELLIPSIS)