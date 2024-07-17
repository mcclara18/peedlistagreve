def main():

    numeros = input("Digite seus números: ")
    
    listanumeros = [int(numero) for numero in numeros.split()]
    
    if not listanumeros:
        print("Insira um número.")
        return
    
    somaimpares = sum(numero for numero in listanumeros if numero % 2 != 0)
    
    print("A soma dos números ímpares é:", somaimpares)

if __name__ == "__main__":
    main()
