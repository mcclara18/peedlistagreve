def main():
    numeros = input("Digite seus números: ")

    listanumeros = [int(numero) for numero in numeros.split()]
    
    if not listanumeros:
        print("Insira um número.")
        return
    
    maiores10 = [numero for numero in lista_numeros if numero > 10]
    
    if maiores10:
        print("maiores do que 10:", maiores10)
    else:
        print("sem números maiores do que 10 na lista.")

if __name__ == "__main__":
    main()
