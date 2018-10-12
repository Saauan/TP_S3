

with open("data", 'r', encoding="utf-8") as stream_text: 
    with open("data", 'rb') as stream_bin: #Q1
        content_text = stream_text.read() #Q2
        content_bin = stream_bin.read()
        print(len(content_text), len(content_bin))
        print(type(content_bin)) #Q3
        print(content_bin[1]) #Q4

#Q5
with open("data.out", 'wb') as stream_bin:
    stream_bin.write(bytes([195, 137]))

#Q6
""" Il possède un seul caractère car les deux octets 
sont encodés en UTF-8 sur un seul caractère.
En effet, les trois premiers bits de la représentation binaire 
de 195 sont 110. Ce qui annonce un caractère codé sur deux octets"""
print(bin(195))

#Q7:
#A chaque fois, les deux fichiers sont identiques, 
#ce qui montre que la conversion a bien fonctionné.

#Q8
#-rw-r--r-- 1 coignion l2 639 Oct  5 11:14 cigale-UTF-8.txt
#-rw-r--r-- 1 coignion l2 624 Oct  5 11:13 cigale-ISO-8859-1.txt
# La différence est de 639 - 624, c'est à dire de 15 octets.
# La différence est dûe au fait que en UTF-8 certains caractères
# sont codés sur plus d'octets qu'en ISO-8859-1

#Q9
#On prend 2 octets et on place en bits de poids fort pour le 1er '110000', et pour le 2nd '10', ensuite
#On place les 2 bits de poids fort de l'octet à convertir à la place des 2 octets de poids faible du 1er octet en UTF-8 et
#On place ses 6 bits restants à la place des 6 bits de poids faible du 2nd octet en UTF-8.
# deux-octet-utf8 = (0xCO | (octet >> 6)) << 8 | (0x80 | b & 0x3F)


#Q10
def isolatinchar_to_utf8(byte):
    """
    Converts an ISO-8859-1 character to an UTF-8 one.

    :param:	byte (int) – A single byte representing an ISO-8859-1 character
    :return:	One or two bytes representing the same character as byte but in UTF-8
    :rtype:	list
    :CU:	0 <= byte < 255
    
    Examples:	
    >>> isolatinchar_to_utf8(65)
    [65]
    >>> isolatinchar_to_utf8(201)
    [195, 137]
    >>> isolatinchar_to_utf8(160)
    [194, 160]
    >>> isolatinchar_to_utf8(255)
    [195, 191]
    """
    if byte >> 7 == 0:
        return [byte]
    else:
        return [0xC0 | (byte >> 6), 0x80 | (byte & 0x3F)]
    
    
#Q11
def isolatin_to_utf8(input,output):
    """
    Converts an ISO-8859-1 file to an UTF-8 one.
    
    :param: input - a file written in ISO-8859-1
            output - a file which will contain the input content converted in UTF-8
    :return: none
    :CU: input is opened in read and binary modes, output is opened in write and binary modes
    """
    while True:
        try:
            c = input.read(1)[0]
            c = isolatinchar_to_utf8(c)
            output.write(bytes(c))
        except IndexError:
            #print("EOF") # DEBUG
            break

#Q12
def convert_file_isolatin_utf8(source, dest):
    """
    Converts ‘ source ‘ file from ISO -8859 -1 encoding to UTF -8.
    The output is written in the ‘ dest ‘ file .
    """
    input_stream = open(source,'rb')
    output_stream = open(dest,'wb')
    isolatin_to_utf8(input_stream,output_stream)
    input_stream.close()
    output_stream.close()

#Q13
def utf8char_to_isolatin(two_bytes):
    """
    Converts an UTF-8 character to a ISO-8859-1 one.

    :param:	two_bytes (list) – The number of bytes to represent a character is variable.
            two_bytes may contain one or two bytes in a list (the list will be of length 1 or 2).
            The bytes are given as integers (between 0 and 255).
    :return:	A list containing only one byte representing the ISO-8859-1 character
    :rtype:	list
    :CU:	1 <= len(two_bytes) <= 2 and each element of the tuple is a byte (value between 0 and 255)
    
    Examples:	
    >>> utf8char_to_isolatin([65])
    [65]
    >>> utf8char_to_isolatin([0xC3, 0x89])
    [201]
    >>> utf8char_to_isolatin([194, 160])
    [160]
    >>> utf8char_to_isolatin([195, 191])
    [255]
    """
    assert(type(two_bytes) == list), "two_bytes is not a list !"
    if len(two_bytes) == 1:
       return two_bytes
    else:
       return [ ((two_bytes[0] & 3) << 6) | (two_bytes[1] & 63) ]

#Q14
def utf8_to_isolatin(instream, outstream):
    """
    Converts an UTF-8 file to an ISO-8859-1 one.
    
    :param: instream - a file written in UTF-8
            outstream - a file which will contain the input content converted in ISO-8859-1
    :return: none
    :CU: input is opened in read and binary modes, output is opened in write and binary modes
    """
    while True:
        try:
            c = [instream.read(1)[0]]
            if c[0] >> 2  == 0x30:
                c.append(instream.read(1)[0])
            c = utf8char_to_isolatin(c)
            assert type(c) == list and len(c) == 1, "c is not correctly converted to ISO"
            outstream.write(bytes(c))
        except IndexError:
            # print("EOF") # DEBUG
            return

#Q15
def convert_file_utf8_isolatin(source, dest): 
    '''
    Converts `source` file from UTF-8 encoding to ISO-8859-1.
    The output is written in the `dest` file.
    ''' 
    input_stream = open(source, 'rb') 
    output_stream = open(dest, 'wb') 
    utf8_to_isolatin(input_stream, output_stream) 
    input_stream.close() 
    output_stream.close()




if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False, optionflags=doctest.ELLIPSIS)
    # Tests:
    # convert_file_isolatin_utf8("cigale-ISO-8859-1.txt", "cigale-UTF-Test.txt")
    # convert_file_utf8_isolatin("cigale-UTF-Test.txt", "cigale-ISO-Test.txt")