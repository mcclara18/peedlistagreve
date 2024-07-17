def main():
    from functools import reduce

    numeros = input("Digite seus números: ")
    
    listanumeros = [int(numero) for numero in numeros.split()]
    
    if not listanumeros:
        print("Insira um número.")
        return
    
    produto = reduce(lambda x, y: x * y, listanumeros)
    
    print("O produto dos números é:", produto)

if __name__ == "__main__":
    main()
