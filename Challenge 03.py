divisor = 0
soma = 0
while True:
    numero = int(input('Digite um número: '))
    soma = soma + numero
    divisor = divisor + 1
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Deseja continuar? (S/N) ')).strip().upper()[0]
    if pergunta == 'N':
        break
print(f'A soma de todos os números digitados é: {soma}. E a média deles é: {soma/divisor}')
