

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

def isolatinchar_to_utf8(byte):