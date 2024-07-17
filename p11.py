def main():
    numeros = input("Digite seus números: ")
    
    listanumeros = [int(numero) for numero in numeros.split()]

    if not listanumeros:
        print("Insira pelo menos um número.")
        return
    
    numeros_pares = [numero for numero in listanumeros if numero % 2 == 0]
    
    if numeros_pares:
        print("pares:", numeros_pares)
    else:
        print("sem números pares.")

if __name__ == "__main__":
    main()
