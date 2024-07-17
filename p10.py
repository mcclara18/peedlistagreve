def main():
    numeros = input("Digite seus números: ")
    
    listanumeros = [int(numero) for numero in numeros.split()]
    
    if not listanumeros:
        print("Insira pelo menos um número.")
        return
    
    media = sum(listanumeros) / len(listanumeros)
    
    print("A média dos números é:", media)

if __name__ == "__main__":

    main()
