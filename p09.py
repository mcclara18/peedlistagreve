def main():
    numeros = input("Digite seus números: ")
    
    listanumeros = [int(numero) for numero in numeros.split()]
    
    if not listanumeros:
        print("Insira um número.")
        return
    
    menornumero = min(listanumeros)
    
    print("O menor número é:", menornumero)

if __name__ == "__main__":
    main()
