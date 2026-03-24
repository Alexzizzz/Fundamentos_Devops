# cajero atm
print ("Hola Cristian introduce tu nip")

nip = int(input("Coloca tu NIP"))
ahorro = 30000

print("Selecciona la opcion que deseas realizar")

ejecutar = True 

while ejecutar:
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")


    opcion = int(input("Escribe la opcion que deseas usar "))

    if opcion == 1:
        print("Tu saldo es de: ",  ahorro)


    elif opcion == 2:
        retiro = int(input("Coloca la cantidad que desdeas realizar: "))
        if retiro <= ahorro :
            ahorro = ahorro - retiro
            print("Retiro exitoso, tu nuevo saldo es de: ", ahorro)
        else:
            print("saldo insuficiente")


    elif opcion == 3:
        deposito= int(input("Coloca la cantidad que quieres depositar"))
        ahorro = ahorro + deposito
        print ("Deposito exitoso, tu nuevo saldo es de: ", ahorro)