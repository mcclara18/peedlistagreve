def palavralonga(palavras):
    palavra = max(palavras, key=len)
    return palavra

def main():
    palavras = input("Digite uma lista de palavras: ").split()
    if palavras:
        palavra = palavralonga(palavras)
        print(f"A palavra mais longa é: {palavra}")
    else:
        print("Digite novamente.")

if __name__ == "__main__":
    main()
