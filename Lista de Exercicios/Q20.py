# programa para achar somar os multiplos de 7 entre 100 e 200


# entrada nao tem
print ("Irei achar os multiplos de um numero entre o intervalo de 1 ate 200")
numero = int(input("Informe o numero: "))
# processamento
soma = 0
for i in range(1,201):
    if i % numero == 0:
        soma = soma + i
        print(f' Multiplo de {numero} - {i}')
        
print(f'Soma dos multiplos de {numero} entre 10 e 200 = {soma}')        