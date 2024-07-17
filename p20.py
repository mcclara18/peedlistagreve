def main():
    numeros = input("Digite seus números: ")
    
    listanumeros = [int(numero) for numero in numeros.split()]
    
    if not listanumeros:
        print("Insira um número.")
        return
    
    ordenada = sorted(listanumeros, reverse=True)
    
    print("A lista ordenada em ordem decrescente é:", ordenada)

if __name__ == "__main__":
    main()
