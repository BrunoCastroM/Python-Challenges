distancias = []
asteroides = {}
cont = 0
soma = 0
while True:
    nome_asteroide = input('Digite o nome do Asteroide: ').strip()
    while not nome_asteroide:
        nome_asteroide = input('Digite o nome do Asteroide: ').strip()
    else:
        for _ in range(5):
            distancia_terra = int(input('Distância em quilômetros da terra: '))
            distancias.append(distancia_terra)
        asteroides[nome_asteroide] = distancias.copy()
        distancias.clear()
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja registrar mais algum asteroide (S/N)? ')).strip().upper()[0]
    if opcao == 'N':
        break
for i in asteroides.items():
    print(i)
for i in asteroides.values():
    for c in i:
        soma += c
for i in asteroides:
    cont += 5
print(f'A média de distância para a Terra do(s) asteroides é de: {soma/cont:.2f}Km')
