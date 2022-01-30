V="aàâäAÂÄeEéèêëËÊiIîïÏÎoOöôÔÖuUûüÛÜyYÿ"    #Définitions des voyelles
C="zrtpqsdfghjklmwxcvbnZRTPQSDFGHJKLMWXCVBN"    #Définitions des consonnes
v=0
c=0
X=input("Ecrire une phrase : ")
for i in range (len(X)):    #Comptage des consonnes et voyelles
    if X[i] in V:
        v=v+1
    elif X[i] in C:
        c=c+1 
print("le nombre de consonnes est",c)
print("le nombre de voyelles est",v)