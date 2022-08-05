# OBS: Visualizei outra maneira de fazer por meio de listas. Porém como essa aula é antes da de listas resolvi fazer com o que tinha até agora.

def seculo(anos):
    if 1 <= anos <= 100:
        return 'O ano que você digitou corresponde ao século I.'
    elif 101 <= anos <= 200:
        return 'O ano que você digitou corresponde ao século II.'
    elif 201 <= anos <= 300:
        return 'O ano que você digitou corresponde ao século III.'
    elif 301 <= anos <= 400:
        return 'O ano que você digitou corresponde ao século IV.'
    elif 401 <= anos <= 500:
        return 'O ano que você digitou corresponde ao século V.'
    elif 501 <= anos <= 600:
        return 'O ano que você digitou corresponde ao século VI.'
    elif 601 <= anos <= 700:
        return 'O ano que você digitou corresponde ao século VII.'
    elif 701 <= anos <= 800:
        return 'O ano que você digitou corresponde ao século VIII.'
    elif 801 <= anos <= 900:
        return 'O ano que você digitou corresponde ao século IX.'
    elif 901 <= anos <= 1000:
        return 'O ano que você digitou corresponde ao século X.'
    elif 1001 <= anos <= 1100:
        return 'O ano que você digitou corresponde ao século XI.'
    elif 1101 <= anos <= 1200:
        return 'O ano que você digitou corresponde ao século XII.'
    elif 1201 <= anos <= 1300:
        return 'O ano que você digitou corresponde ao século XIII.'
    elif 1301 <= anos <= 1400:
        return 'O ano que você digitou corresponde ao século XIV.'
    elif 1401 <= anos <= 1500:
        return 'O ano que você digitou corresponde ao século XV.'
    elif 1501 <= anos <= 1600:
        return 'O ano que você digitou corresponde ao século XVI.'
    elif 1601 <= anos <= 1700:
        return 'O ano que você digitou corresponde ao século XVII.'
    elif 1701 <= anos <= 1800:
        return 'O ano que você digitou corresponde ao século XVIII.'
    elif 1801 <= anos <= 1900:
        return 'O ano que você digitou corresponde ao século XIX.'
    elif 1901 <= anos <= 2000:
        return 'O ano que você digitou corresponde ao século XX.'
    elif 2001 <= anos <= 2100:
        return 'O ano que você digitou corresponde ao século XXI.'


ano = int(input('Digite o ano que você deseja saber o século: '))
print(seculo(ano))
