
#Creado por Eyder Huayta para el proyecto de Cisco - 2020

print("#===================#")
print("       SUDOKU")
print("#===================#")
print("\nEste programa no es para jugar,")
print("solo fue hecho para visualizar un tablero ya completado de forma random.\n")
juego=True
def Juego():
    sudoku=[[0,1,2,3,4,5,6,7,8],[3,4,5,6,7,8,0,1,2],[6,7,8,0,1,2,3,4,5],[1,2,3,4,5,6,7,8,0],[4,5,6,7,8,0,1,2,3],[7,8,0,1,2,3,4,5,6],[2,3,4,5,6,7,8,0,1],[5,6,7,8,0,1,2,3,4],[8,0,1,2,3,4,5,6,7]]
    import random
    cont=0
    a=random.randint(1,9)
    for i in sudoku:
        for b in i:
            z=a
            new=b+z
            sudoku[sudoku.index(i)][cont]=new
            z=0
            cont+=1
        cont=0
    for a in range(1,10):
        z=sudoku[-(a)]
        for i in z:
            if i > 9:
                i-=9
                
                print(" ",i,end=" ")
            else:
                print(" ",i,end=" ")
        print()
        print()
Juego()
while juego:
    elec=input("¿Quieres imprimir otro tablero?\n")
    print()
    elec=elec.lower()
    if elec== "si":
        Juego()
    elif elec == "no":
        juego=False
    else:
        print("¿Que?, Te oreguntaré de nuevo...")

print("Fin :)")

#Perdon por no ser tan "random"
