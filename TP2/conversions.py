'''
@author FIL - FST - Univ. Lille
'''
import float_coding
import timeit

def integer_to_digit(integer):
    '''
    Convert an integer in a hexadecimal digit

    :param integer:
    :type integer: int
    :return: the character representing the hexadecimal digit
    :rtype: str
    :CU: integer >= 0 and integer < 16
    :Examples:
    
    >>> integer_to_digit(15)
    'F'
    >>> integer_to_digit(0)
    '0'
    >>> integer_to_digit(-1)
    Traceback (most recent call last):
    ...
    AssertionError: Integer is Negative or Too Large
    '''
    assert integer in set(i for i in range(16)) and type(integer) == int, "Integer is Negative or Too Large"
    if 0 <= integer <= 9:
        return chr(ord('0') + integer)
    else:
        return chr(ord('7') + integer)
    
    
def integer_to_string(integer, base):
    '''
    Gives the representation in base `base` of the integer `integer`.

    :param integer: the integer we want to represent
    :type integer: int
    :param base: the base in which the integer must be represented
    :type base: int
    :return: The string representation of the integer given in parameter\
    in base `base`.
    :rtype: str
    :CU: base >= 2 and base <= 16 and integer >= 0
    :Examples:

    >>> integer_to_string(1331, 2)
    '10100110011'
    >>> integer_to_string(1331, 8)
    '2463'
    >>> integer_to_string(1331, 16)
    '533'
    >>> integer_to_string(250, 16)
    'FA'
    >>> integer_to_string(250, 10)
    '250'
    >>> integer_to_string(1, 10)
    '1'
    >>> integer_to_string(0, 2)
    '0'
    '''
    assert integer >= 0 and int(integer)==integer and type(integer) == int, "Integer is Negative or Not an Integer"
    assert base in set(i for i in range(2, 17)), "Not a valid base"
    convertString = "0123456789ABCDEF"
    res = ""
    while integer >= base:
        res = convertString[integer % base] + res
        integer = integer // base
    res = convertString[integer] + res
    return res
    
def display_20_integers():
    '''
    Display representations of the first 20 positive integers in bases 10, 2,
    8 and 16.
    
    >>> display_20_integers()
    0  : 0     0  0 
    1  : 1     1  1 
    2  : 10    2  2 
    3  : 11    3  3 
    4  : 100   4  4 
    5  : 101   5  5 
    6  : 110   6  6 
    7  : 111   7  7 
    8  : 1000  10 8 
    9  : 1001  11 9 
    10 : 1010  12 A 
    11 : 1011  13 B 
    12 : 1100  14 C 
    13 : 1101  15 D 
    14 : 1110  16 E 
    15 : 1111  17 F 
    16 : 10000 20 10
    17 : 10001 21 11
    18 : 10010 22 12
    19 : 10011 23 13
    20 : 10100 24 14
    '''
    for nbr in range(21):
        print("{:2s} : {:5s} {:2s} {:2s}".format(str(nbr),
        integer_to_string(nbr, 2),
        integer_to_string(nbr, 8),
        integer_to_string(nbr, 16)))
    
def power_two(n):
    '''
    Compute 2^n

    :param n: The power of two
    :type n: int
    :return: The value of 2^n
    :rtype: int
    :CU: n >= 0
    :Examples:

    >>> power_two(0)
    1
    >>> power_two(10)
    1024
    '''
    assert type(n) == int, "Your number entered is not an integer"
    if n == 0:
        return 1
    else:
        return 2 << n-1
    
def is_even(n):
    '''
    A predicate that tells if the integer n is even.

    :param n: the integer to test
    :type n: int
    :return: True iff n is even (can be divided by 2)
    :rtype: bool
    :CU: n >= 0
    :Examples:

    >>> is_even(0)
    True
    >>> is_even(2)
    True
    >>> is_even(1)
    False
    >>> is_even(43)
    False
    >>> is_even(42)
    True
    '''
    assert type(n) == int, "Your number entered isn't an int"
    return n & 1 == 0
    
def integer_to_binary_str(integer):
    '''
    Get a binary representation of an integer.

    :param integer: the integer to be converted in binary
    :type integer: int
    :rtype: str
    :return: Return the binary representation (as a string) of `integer`
    :CU: integer >= 0
    :Examples:

    >>> integer_to_binary_str(1)
    '1'
    >>> integer_to_binary_str(2)
    '10'
    >>> integer_to_binary_str(53)
    '110101'
    '''
    assert type(integer) == int and integer >= 0, "Your number entered isn't an int"
    return bin(integer)[2:]
    
def binary_str_to_integer(bin_str):
    '''
    Inverse function of :py:func:`conversions.integer_to_binary_str`

    :param bin_str: The input binary string
    :type bin_str: str
    :return: The integer whose binary representation is `bin_str`
    :rtype: int
    :CU: `bin_str` is a binary string (containing only 0s or 1s).
    :Examples:
    
    >>> binary_str_to_integer("0")
    0
    >>> binary_str_to_integer("110101")
    53
    >>> binary_str_to_integer("10000000")
    128
    '''
    assert type(bin_str) == str, "Your bin number isn't a string"
    return int(bin_str,2)
    
def most_least_significant_bits_str(byte):
    '''
    Return an integer made with the most and least significant bits of the
    `byte` given in parameter.

    :param byte: (int) A byte
    :type byte: int
    :return: An integer whose binary representation is made of the most and \
    least significant bits of the `byte`.
    :rtype: int
    :CU: 0 <= byte < 256
    :Examples:

    >>> most_least_significant_bits_str(0)
    0
    >>> most_least_significant_bits_str(255)
    3
    >>> most_least_significant_bits_str(101)
    1
    >>> most_least_significant_bits_str(100)
    0
    >>> most_least_significant_bits_str(128)
    2
    >>> most_least_significant_bits_str(129)
    3
    '''
    assert byte <= 255 and byte >= 0 and type(byte) == int, "The parameter is not a correct byte"
    byte_str = integer_to_string(byte, 2)
    res = 0
    if len(byte_str) == 8:
        res = 2
    res += int(byte_str[-1])
    return res

    
def most_least_significant_bits(byte):
    '''
    Return an integer made with the most and least significant bits of the
    `byte` given in parameter.

    :param byte: A byte
    :type byte: int
    :return: An integer whose binary representation is made of the most and \
    least significant bits of the `byte`.
    :rtype: int
    :CU: 0 <= byte < 256
    :Examples:

    >>> most_least_significant_bits(0)
    0
    >>> most_least_significant_bits(255)
    3
    >>> most_least_significant_bits(101)
    1
    >>> most_least_significant_bits(100)
    0
    >>> most_least_significant_bits(128)
    2
    >>> most_least_significant_bits(129)
    3
    '''
    assert byte <= 255 and byte >= 0 and type(byte) == int, "The parameter is not a correct byte"
    return (byte & 1) + (byte >> 7 ) * 2

    
def isolate_bit(value, pos):
    '''
    Give the value of one bit at position `pos` in the binary representation of \
    `value`

    :param value: The binary representation where we want to extract a single bit. This value is stored as an integer.
    :type value: int
    :param pos: The position of the bit to retrieve. 0 means least significant bit.
    :type pos: int
    :return: The bit at the given position in the binary representation of `value`
    :rtype: int
    :CU: pos >= 0
    :Examples:

    >>> isolate_bit(0, 0)
    0
    >>> isolate_bit(0, 5)
    0
    >>> isolate_bit(4, 10)
    0
    >>> isolate_bit(4, 0)
    0
    >>> isolate_bit(4, 2)
    1
    >>> isolate_bit(5, 0)
    1
    >>> isolate_bit(5, 2)
    1
    >>> isolate_bit(5, 5)
    0
    '''
    return (value >> pos) & 1
    
    
def isolate_bits(value, positions):
    '''
    Get several bits from the binary representation of `value`.
    The bit positions we need to get are given by `positions`.

    :param value: The binary representation where we want to extract some bits. This value is stored as an integer.
    :type value: int
    :param pos: A list of positions of the bits to retrieve. 0 means least significant bit.
    :type pos: most
    :return: An integer whose binary representation corresponds to the extracted bits\
    in the same order as in `positions`: the first extracted bit will be the most \
    significant bit in the returned value
    :rtype: int
    :CU: len(posisitions) > 0 and each value of positions is >= 0
    :Examples:

    >>> isolate_bits(0, [0, 5, 2])
    0
    >>> isolate_bits(4, [0, 2, 4])
    2
    >>> isolate_bits(4, [2, 0, 4])
    4
    >>> isolate_bits(4, [0, 4, 2])
    1
    >>> isolate_bits(5, [0, 2])
    3
    >>> isolate_bits(5, [2, 0])
    3
    >>> isolate_bits(5, [2, 1])
    2
    >>> isolate_bits(5, [0, 1])
    2
    >>> isolate_bits(0b110110110, [8, 5, 2])
    7
    >>> isolate_bits(0b110110110, [8, 6, 3])
    4
    >>> isolate_bits(0b110110110, [8, 6, 2])
    5
    '''
    res = ""
    for i in positions:
        res += str((value >> i) & 1) 
    res = binary_str_to_integer(res)
    return res

def mask1(length):
    '''
    Return an integer whose binary representation is only made of `length`\
    consecutive  1s.

    :param length: Number of 1s in the binary representation
    :type length: int
    :return: See the description of the function
    :rtype: int
    :CU: length >= 0
    :Examples:

    >>> mask1(0)
    0
    >>> mask1(1)
    1
    >>> mask1(2)
    3
    >>> mask1(3)
    7
    >>> mask1(10)
    1023
    '''
    return (1 << length) -1
    
def isolate_consecutive_bits(value, msb_pos, nb_bits):
    '''
    Get several consecutive bits from the binary representation of `value`.
    We will get `nb_bits` starting with the most significant bit at position
    `msb_pos`.

    :param value: The binary representation where we want to extract consecutive bits. This value is stored as an integer.
    :type value: int
    :param msb_pos: The position of the most significant bit to be extracted
    :type msb_pos: int
    :param nb_bits: The number of consecutive bits to extract
    :type nb_bits: int
    :return: An integer whose binary representation corresponds to the consecutive\
    extracted bits starting at `msb_pos` for the most significant bit and extracting\
    the `nb_bits` following bits in total.
    :rtype: int
    :CU: msb_pos >= 0 and msb_pos + 1 >= nb_bits
    :Examples:
    
    >>> isolate_consecutive_bits(4, 2, 2)
    2
    >>> isolate_consecutive_bits(4, 2, 1)
    1
    >>> isolate_consecutive_bits(4, 1, 2)
    0
    >>> isolate_consecutive_bits(0b100110110, 5, 3)
    6
    >>> isolate_consecutive_bits(0b100110110, 5, 4)
    13
    >>> isolate_consecutive_bits(0b100110110, 5, 2)
    3
    >>> isolate_consecutive_bits(0b110110110, 8, 2)
    3
    >>> isolate_consecutive_bits(0b110110110, 9, 2)
    1
    >>> isolate_consecutive_bits(0b110110110, 9, 3)
    3
    '''
    return (value >> (msb_pos - nb_bits + 1)) & mask1(nb_bits)
    # value >> (msb_pos - nb_bits + 1) Removes the bits we don't want on the right part.
    # & mask1(nb_bits) Removes the bits we don't want on the left part.

def float_sign(value):
    '''
    Return the sign of a float represented under the 
    64-bit IEEE-754 standard.

    :param value: The value whose binary representation follows the IEEE-754 standard
    :type value: int
    :return: -1 if the float is negative 1 otherwise
    :rtype: int
    :CU: value is represented on 64 bits at most.
    :Examples:

    >>> float_sign(float_coding.floatbin(3.5))
    1
    >>> float_sign(float_coding.floatbin(-3.5))
    -1
    '''
    if value >> 63 == 1: # Si le bit de poids fort de value est de 1
        return -1
    else:
        return 1

def float_exponent(value):
    '''
    Returns the exponent e of a float f =
    (-1)^s * 2^e * m.

    The float is represented under the 64-bit IEEE 754 standard in which the
    exponent takes 11 bits.

    :param value: binary representation of the float
    :type value: int
    :return: The exponent of the float (the exponent is in between -1022 and 1023)
    :rtype: int
    :CU: value is represented on 64 bits at most.
    :Examples: 

    >>> float_exponent(float_coding.floatbin(3.5))
    1
    >>> float_exponent(float_coding.floatbin(5))
    2
    >>> float_exponent(float_coding.floatbin(1/10))
    -4
    >>> float_exponent(float_coding.floatbin(1.2))
    0
    '''
    # E = e + 2**(w-1) - 1; then, e = E - 2**(w-1) - 1
    # With E an integer (encoded exponent), 
    # e the exponent of the float, 
    # and w the number of bits allocated to E
    return isolate_consecutive_bits(value, 52+11-1, 11) - 2**(11-1) + 1


def float_mantissa(value):
    '''
    Returns the mantissa m of a float f =
    (-1)^s * 2^e * m.

    The float is represented under the 64-bit IEEE 754 standard in which the
    mantissa takes 52 bits.

    :param value: binary representation of the float
    :type value: int
    :return: The mantissa of the float (2 > mantissa >= 1)
    :rtype: float
    :CU: value is represented on 64 bits at most.
    :Examples: 

    >>> float_mantissa(float_coding.floatbin(3.5))
    1.75
    >>> float_mantissa(float_coding.floatbin(4))
    1.0
    >>> float_mantissa(float_coding.floatbin(-3.5))
    1.75
    >>> float_mantissa(float_coding.floatbin(14))
    1.75
    >>> float_mantissa(float_coding.floatbin(24))
    1.5
    '''
    # m = 1 + 2**(-t) * M, and M = (m-1)/2**(-t)
    # With t the number of bits allocated to M,
    # M the integer on which m is encoded
    return isolate_consecutive_bits(value, 52-1, 52) * 2**(-52) + 1


def float_notation(float_value):
    '''
    Return the sign, exponent and mantissa of a float

    :param float_value: the float value which has to be decomposed, in decimal
    :type float_value: float
    :return: The sign s, exponent e and mantissa m such that float_value = s * 2^e * m
    :rtype: tuple
    :CU: None
    :Examples:

    >>> float_notation(3.5)
    (1, 1, 1.75)
    >>> float_notation(-3.5)
    (-1, 1, 1.75)
    >>> float_notation(14)
    (1, 3, 1.75)
    >>> float_notation(24)
    (1, 4, 1.5)
    '''
    v = float_coding.floatbin(float_value) # IEEE-754 binary representation of the float
    return (float_sign(v), float_exponent(v), float_mantissa(v))
    
def change_a_bit(value, position):
    '''
    Changes a bit in an integer

    :param value: value whose binary representation must be changed
    :type binary: int
    :param position: The position at which the bit must be changed in `value`. Position 0 is the least significant bit.
    :type position: int
    :return: The modified value where the bit at position `position`\
    has been changed
    :rtype: int
    :CU: 0 <= position
    :Examples:

    >>> change_a_bit(4, 0)
    5
    >>> change_a_bit(4, 1)
    6
    >>> change_a_bit(4, 2)
    0
    >>> change_a_bit(4, 3)
    12
    '''
    # 1 << position creates a binary number with one 1 and `position` 0 behind
    # "^" is a xor
    return value ^ (1 << position)

def change_a_bit_in_float(value, bit_position):
    '''
    Changes a bit in the IEEE-754 64-bit float representation.

    :param value: The float we want to modify
    :type value: float
    :param bit_position: The position (in the binary IEEE-754 representation)\
    where the bit will be modified. Position 0 means least significant bit
    :type bit_position: int
    :return: the value of `value` where the bit at position `bit_position`\
    in its IEEE-754 binary representation has been changed
    :rtype: float
    :CU: bit_position >= 0 and bit_position < 64
    :Examples:

    >>> change_a_bit_in_float(3.5, 63)
    -3.5
    >>> change_a_bit_in_float(3.5, 52)
    7.0
    >>> change_a_bit_in_float(3.5, 51)
    2.5
    '''
    v_bin = float_coding.floatbin(value) # IEEE-754 binary representation of the float
    v_bin = change_a_bit(v_bin, bit_position)
    return float_coding.binfloat(v_bin) # Decimal representation of the float

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False, optionflags=doctest.ELLIPSIS)
    # time1 = timeit.timeit('most_least_significant_bits(255)',
    #         setup = "from __main__ import most_least_significant_bits",
    #         number = 100000) 
    # time2 = timeit.timeit('most_least_significant_bits_str(255)',
    #         setup = "from __main__ import most_least_significant_bits_str",
    #         number = 100000)
    # print(time1, time2)