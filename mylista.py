#ejemplo de uso de lista
misnovios=["Adriel","Bakugo","Tsukkishima"]
misnumeros=[11,27,22]
#mostrando mis novios
print(misnovios)
#mostrando mis numeros
print(misnumeros)
print("----Accediendo a los elementos de lista--- ")
print(misnovios[-2])
if "sero" in misnovios:
    print("si, esta en la lista de mis novios")
else:
    print("chale,no es mi novio")
    print("Numero de novios")
    Nnovios=len(misnovios)
    print(f"numero de novios:{Nnovios}")
print( "CICLO FOR EN LISTAS")
posicion=0
for medianaranja in misnovios:
    print(posicion," ",medianaranja)
    posicion=posicion+1