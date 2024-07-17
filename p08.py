def main():
    numeros = input("Digite seus números: ")
    
    listanumeros = [int(numero) for numero in numeros.split()]
    
    if not listanumeros:
        print("Insira um número.")
        return
    
    maiornumero = max(listanumeros)
    
    print("O maior número é:", maiornumero)

if __name__ == "__main__":
    main()
