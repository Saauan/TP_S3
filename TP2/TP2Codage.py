import conversions, float_coding
#EXERCICE 1 - Q1
#On prend comme entiers de référence 35, 243 & 124

print("{:b}".format(35)); print("{:x}".format(35)); print("{:o}".format(35)); print("{:X}".format(35))
print("")#############
print("{:b}".format(243)); print("{:x}".format(243)); print("{:o}".format(243)); print("{:X}".format(243))
print("")#############
print("{:b}".format(124)); print("{:x}".format(124)); print("{:o}".format(124)); print("{:X}".format(124))
print("")#############

#Dans l'ordre (b, x, o, X), ils représentent le binaire, l'hexadecimal avec les lettres en minuscules,
#l'octal et enfin l'hexadecimal avec les lettres en MAJUSCULES.



#Q2
print("1331 s'écrit :")
print(bin(1331)[2:], "en binaire"); print(oct(1331)[2:], "en octal"); print(hex(1331)[2:], "en hexadecimal")
print("")#############



#Q3
print(chr(ord('0') + 1)); print(chr(ord('0') + 5)); print(chr(ord('0') + 9)); print(chr(ord('0') + 11))
print("")#############
#Si 0 <= n <= 9, l'expression vaut n, sinon il vaut un autre caractère, comme une ponctuation.



#Q4
print(chr(ord('7') + 10)); print(chr(ord('7') + 15))
print("")#############
#On remplace donc simplement le '0' par '7' ce qui nous permet de passer les ponctuations et d'arriver aux 6 premières lettres



#Q5, Q6 & Q7 dans le fichier conversions.py
conversions.display_20_integers()
print("")#############


#EXERCICE 2 - Q9
#n << 1 permet de doubler n tandis que n >> 1 fait une division partie entière par 2



#Q10, Q11, Q12 et Q13 dans le fichier conversions.py
# most_least_significant_bits est la plus rapide des deux fonctions (0.5s contre 6.2s)
# On en conclue donc que les opérateurs logiques sont très efficaces.
"A faire : Q15 à Q16, Q18"



#Q19
f1, f2, f3 = float_coding.floatbin(4), float_coding.floatbin(8), float_coding.floatbin(12)
print(f1,"|",conversions.integer_to_string(f1,2),"|",len(conversions.integer_to_string(f1,2)))
print(f2,"|",conversions.integer_to_string(f2,2),"|",len(conversions.integer_to_string(f2,2)))
print(f3,"|",conversions.integer_to_string(f3,2),"|",len(conversions.integer_to_string(f3,2)))
print("")#############

"Pourquoi certain bits changent + pourquoi pas 64bits ? (bit de signe?)"


#Q20
f1 +=1 ; f2 +=1 ; f3 +=1
print(f1,"|",float_coding.binfloat(f1))
print(f2,"|",float_coding.binfloat(f2))
print(f3,"|",float_coding.binfloat(f3))
print("")#############
#On obtient de nouveau 4,8,12 cependant ils ont respectivement subi une addition de 1.10**-15 ou 2.10**-15.



"Q22 & Q23 à faire"



