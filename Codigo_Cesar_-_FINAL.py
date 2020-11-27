#Programa de Eyder Huayta hecho para Cisco - 2020
print("====================")
print("Desencriptador Cesar")
print("====================")

mensaje1= input("Ingresa la frase a desencriptar, por favor :)\nRecuerde que tiene que tener \"sentido\"\n")
mensaje=mensaje1

from statistics import mode
from re import sub
suba=" +"
mensaje= sub(suba,"",mensaje)

lista=[]
final=[]

diccionarioM={91:65,92:66,93:67,94:68,95:69,96:70,97:71,98:72,99:73,100:74}
diccionariom={123:97,124:98,125:99,126:100,127:101,128:102,129:103,130:104}
diccionario={44:44,32:32,46:46}
suma=0
for i in mensaje:
    a= ord(i)
    lista.append(a)
    
condition=mode(lista)

if 69 < condition and condition < 91:
    condition-=26
    while not condition == 69:
        condition+=1
        suma+=1
elif 64 < condition and condition < 69:
    while not condition == 69:
        condition+=1
        suma+=1
elif 96 < condition and condition < 101:
    while  not condition == 101:
        condition+=1
        suma+=1
elif 101 < condition and condition < 123:
    condition-=26
    while not condition == 101:
        condition+=1
        suma+=1

'''
elif condition == 44 or condition == 32 or condition == 46:
    cacauate = 1
'''
del lista
lista=[]

for i in mensaje1:
    a= ord(i)
    if a == 44 or a == 32 or a==46:
        lista.append(a)
    else:
        a= ord(i)+suma
        lista.append(a)


for a in lista:
        if a== 44 or a== 32 or a==46:
            lista[lista.index(a)]= diccionario[a]
        elif a > 90 and a < 101:
            lista[lista.index(a)]= diccionarioM[a]
    
        elif a > 122 and a <130:
            lista[lista.index(a)]=diccionariom[a]


for i in lista:
    a= chr(i)
    final.append(a)

print("El mensaje desencriptado es:")
for i in final:
    print(i, end="",sep="")
print("\nY la llave es igual a: ",suma)
print("Fin :)")
#Ignorar la version beta u.u


'''
while mode(lista)!=101 or mode(lista)!=69:
    del lista
    lista=[]
    
    for i in mensaje1:
        if  i== 44 or i== 32 or i==46:
            a= ord(i)
        else:
            a= ord(i)+suma
            lista.append(a)

    for a in lista:
        if a== 44 or a== 32 or a==46:
            lista[lista.index(a)]= diccionario[a]
        elif a > 90 and a < 101:
            lista[lista.index(a)]= diccionarioM[a]
    
        elif a > 122 and a <130:
            lista[lista.index(a)]=diccionariom[a]


del lista
lista=[]

for i in mensaje1:
    a= ord(i)
    lista.append(a)
for i in lista:
    a= chr(i)
    final.append(a)

print("El mensaje desencriptado es:")
for i in final:
    print(i, end="",sep="")
print("\nY la llave es igual a: ",suma)
'''
