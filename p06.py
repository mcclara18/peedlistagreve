numeros = int(input("Digite seus números"))

numlista = 0

for c in range (numeros):
    num = int(input('Digite um numero: '))
    numlista+=num 
    
print(f"A soma é:", numlista)