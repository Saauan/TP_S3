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





#Q19
f1, f2, f3 = float_coding.floatbin(4), float_coding.floatbin(8), float_coding.floatbin(12)
print(f1,"|",conversions.integer_to_string(f1,2),"|",len(conversions.integer_to_string(f1,2)))
print(f2,"|",conversions.integer_to_string(f2,2),"|",len(conversions.integer_to_string(f2,2)))
print(f3,"|",conversions.integer_to_string(f3,2),"|",len(conversions.integer_to_string(f3,2)))
print("")#############

""" Ces représentations binaires sont longues de 63 bits.
Elle n'est pas systématiquement de 64 bits, car le premier bit (celui du signe) peut
être égal à 0, tout comme les premiers bits de l'exposant. Alors, dans ces cas là,
ils ne sont pas affichés. """
""" De la même manière, certains bits changent parceque l'exposant change"""


#Q20
f1 +=1 ; f2 +=1 ; f3 +=1
print(f1,"|",float_coding.binfloat(f1))
print(f2,"|",float_coding.binfloat(f2))
print(f3,"|",float_coding.binfloat(f3))
print("")#############
# On obtient de nouveau 4,8,12 cependant ils ont respectivement subi une addition de 1.10**-15 ou 2.10**-15.
# Tout cela parceque le "1" qu'on a ajouté s'est retrouvé sur la mantisse du nombre flottant.


#Q27
f1 = conversions.change_a_bit_in_float(2, 0)
f2 = conversions.change_a_bit_in_float(2, 51)
f3 = conversions.change_a_bit_in_float(2, 55)
f4 = conversions.change_a_bit_in_float(2, 52) # Not asked in the question
for f,i in ((f1,0), (f2,51), (f3,55), (f4,52)):
    print("When we change the bit at the position {} the float is equal to {}".format(i, f))

# Quand on change les bits 0 et 51, on change directement la mantisse.
# Quand on change le bit 55, on change la valeur de l'exposant.
# CHECK LA REPONSE ICI.

#Q28
print("\nChecking if .1 + .2 != .3:")
print(float_coding.floatbin(.1) + float_coding.floatbin(.2) != float_coding.floatbin(.3), "\n")
# C'est vrai.

#Q29
for i in (.1, .2, .3):
    print("Checking the values given by `float_notation` for {} are correct".format(i))
    s, e, m = conversions.float_notation(i)
    res = (s * 2**e * m) == i
    print("according to `float_notation`, s, e and m are {}, {} and {}. Which is... {}".format(s, e, m, res))

print("")

#Q30
for i in (.1, .2, .3):
    sem = conversions.float_notation(i) 
    print('({0[0]:d}, {0[1]:d}, {0[2]:.20f})'.format(sem))

# On a .1 + .2 != .3 parceque leur valeurs binaires sont tronquées. 
# On a donc une perte d'informations lors de la comparaison