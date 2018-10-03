import struct
import doctest

def floatbin(value):
    '''
    Returns an integer corresponding to the binary representation of the
    float given in parameter.
    :param value: the float to convert
    :type value: float
    :return: An integer whose binary representation is equal to the float's
             binary representation.
             The float is represented on 64 bits.
    :rtype: int
    :CU: None
    
    Examples:

    >>> '{:b}'.format(floatbin(3.5))
    '100000000001100000000000000000000000000000000000000000000000000'
    >>> '{:b}'.format(floatbin(-3.5))
    '1100000000001100000000000000000000000000000000000000000000000000'
    '''
    floatbytes = struct.pack('>d', value)
    length = len(floatbytes)
    return sum([b << (8 * (length - i - 1)) for i, b in enumerate(floatbytes)])

def binfloat(value):
    '''
    Returns the float that have the same binary representation as the integer
    given in parameter.

    :param value: The integer that will be converted
    :type value: int
    :return: A float whose binary representation is the same as the integer value
    :rtype: float
    :CU: value should not be represented on more than 64 bits

    Examples:
    >>> binfloat(floatbin(3.5))
    3.5
    >>> binfloat(floatbin(-3.5))
    -3.5
    '''

    byte_list = []
    mask = 0xFF
    while value > 0:
        byte_list.insert(0, value & mask)
        value >>= 8
        
    for i in range(len(byte_list), 8):
        byte_list.insert(0,0)
    return struct.unpack('>d', bytes(byte_list))[0]