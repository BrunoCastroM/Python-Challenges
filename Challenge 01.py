dia = int(input('Em que dia você nasceu?: '))
mes = int(input('Digite o mês de nascimento (número): '))
if mes == 1 and 21 <= dia <= 31 or mes == 2 and 1 <= dia <= 18:
    print('Seu signo é: Aquário!')
elif mes == 2 and 19 <= dia <= 29 or mes == 3 and 1 <= dia <= 20:
    print('Seu signo é: Peixes!')
elif mes == 3 and 21 <= dia <= 31 or mes == 4 and 1 <= dia <= 20:
    print('Seu signo é: Áries!')
elif mes == 4 and 21 <= dia <= 30 or mes == 5 and 1 <= dia <= 20:
    print('Seu signo é: Touro!')
elif mes == 5 and 21 <= dia <= 31 or mes == 6 and 1 <= dia <= 20:
    print('Seu signo é: Gêmeos!')
elif mes == 6 and 21 <= dia <= 30 or mes == 7 and 1 <= dia <= 22:
    print('Seu signo é: Cancer!')
elif mes == 7 and 23 <= dia <= 31 or mes == 8 and 1 <= dia <= 22:
    print('Seu signo é: Leão!')
elif mes == 8 and 23 <= dia <= 31 or mes == 9 and 1 <= dia <= 22:
    print('Seu signo é: Virgem!')
elif mes == 9 and 23 <= dia <= 30 or mes == 10 and 1 <= dia <= 22:
    print('Seu signo é: Libra!')
elif mes == 10 and 23 <= dia <= 31 or mes == 11 and 1 <= dia <= 21:
    print('Seu signo é: Escorpião!')
elif mes == 11 and 22 <= dia <= 30 or mes == 12 and 1 <= dia <= 21:
    print('Seu signo é: Sagitário')
elif mes == 12 and 22 <= dia <= 31 or mes == 1 and 1 <= dia <= 20:
    print('Seu signo é: Capricórnio')
else:
    print('Dados inválidos!')
    