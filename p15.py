def main():
    numeros = input("Digite seus números: ")

    listanumeros = [int(numero) for numero in numeros.split()]

    if not listanumeros:
        print("Insira um número.") 
        return
    
    menorque5 = [numero for numero in listanumeros if numero < 5]
    
    if menorque5:
        print("menores do que 5:", menorque5)
    else:
        print("sem números menores do que 5.")

if __name__ == "__main__":
    main()
