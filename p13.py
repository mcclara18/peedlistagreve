def main():
    palavras = input("Digite suas palavras: ")
    
    listapalavras = palavras.split()
    
    palavras_com_a = [palavra for palavra in listapalavras if palavra.lower().startswith('a')]
    
    if palavras_com_a:
        print("Palavras que começam com 'a':", palavras_com_a)
    else:
        print("Sem palavras que começam com 'a'.")

if __name__ == "__main__":
    main()
