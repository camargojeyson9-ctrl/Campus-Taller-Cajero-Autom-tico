def consultar_saldo (Balance):
    Balance = saldo
    return Balance

def depositar (Ingreso):
    deposito = saldo + Ingreso
    return deposito


def Retirar (Retiro):
    retiro = saldo - Retiro
    return retiro


saldo = 1000
deposito = 0
retiro = 0

print("\n---BIENVENIDO AL CAJERO AUTOMATICO---")

while True:
    
    print("\nMenu principal, Escoge una opcion:")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")


    opcion = int(input("Escoge una opcion del 1 al 4: "))

    if opcion == 1:
        print("\nEscogiste la opcion 1, a continuacion vas a ver tu saldo:")
        print("---BALANCE DE TU CUENTA---")
        balance_cuenta = consultar_saldo(saldo)
        print("Tu balance actual es:", balance_cuenta)

    elif opcion == 2:
        print("\nSeleccionaste la opcion de deposito")
        deposito = int(input("Ingresa el monto que deseas depositar: "))
        if deposito > 0:
            saldo = depositar(deposito)
            print("Felicidades, deposito guardado con exito ")

        else:
            print("[!] El monto debe ser mayor a 0")

    elif opcion == 3:
        print("\nSeleccionaste la opcion de retiro")
        retiro = int(input("Ingresa el valor del retiro que deseas realizar: "))
        if retiro < saldo and retiro > 0:
            saldo = Retirar(retiro)
            print("Confirmo retiro realizado con exito")
        else:
            print("[!] El retiro debe ser mayor que 0 y menor que tu saldo.")

    elif opcion == 4:
        print("\nSeleccionaste la opcion de salir")
        print("\nGracias por usar el cajero")
        print("Nos vemos pronto")
        break

    else:
        print("\nERROR")
        print("[!]Escoge una opcion valida del (1 al 4)")


