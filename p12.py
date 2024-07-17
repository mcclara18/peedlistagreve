def main():
    numeros = input("Digite seus números: ")
    
    listanumeros = [int(numero) for numero in numeros.split()]
    
    if not listanumeros:
        print("Insira pelo menos um número.")
        return
    
    numeros_impares = [numero for numero in listanumeros if numero % 2 != 0]
    
    if numeros_impares:
        print("ímpares :", numeros_impares)
    else:
        print("Sem números ímpares.")

if __name__ == "__main__":
    main()
