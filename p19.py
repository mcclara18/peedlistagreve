def main():
    numeros = input("Digite seus números: ")
    
    listanumeros = [int(numero) for numero in numeros.split()]
    
    if not listanumeros:
        print("Insira um número.")
        return
    
    ordenada = sorted(listanumeros)
    
    print("A lista ordenada em ordem crescente é:", ordenada)

if __name__ == "__main__":
    main()
