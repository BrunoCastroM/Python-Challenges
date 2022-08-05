soma = 0
print('Promoção!!! Frete grátis pra compras a partir de R$ 200,00!!!')
while True:
    produto = int(input('Digite o valor do produto que você quer comprar: '))
    pergunta = ' '
    soma = soma + produto
    while pergunta not in 'SN':
        pergunta = str(input('Deseja passar mais algum produto (S/N)? ')).strip().upper()[0]
    if pergunta == 'N':
        break
if soma >= 200:
    print('Você ganhou frete grátis para essa compra!')
else:
    print('Infelizmente você não ganhou o frete grátis.')
print(f'O valor total dos produtos é de: R${soma:.2f}')
