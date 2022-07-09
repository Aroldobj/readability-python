from cs50 import get_string

while True:
    str = get_string('Texto: ')
    índice = 0
    eu = 0
    alfabetos = 0
    dígitos = 0
    especial = 0
    palavras = 1
    frases = 0
    if(str):
        for i in range(len(str)):
            if(str[i].isalpha()):
                alfabetos += 1
            elif(str[i].isnumeric()):
                dígitos += 1
            elif(str[i] == ' ' and str[i + 1]):
                palavras += 1
            elif(str[i] == '?' or str[i] == '!' or str[i] == '.'):
                frases += 1
            else:
                especial += 1
        # Obter L - o número médio de letras por 100 palavras no texto
        L = float(alfabetos / palavras * 100)

        # Obter S - o número médio de frases por 100 palavras no texto
        S = float(frases / palavras * 100)

        # Legibilidade
        índice = round((float)(0.0588 * L - 0.296 * S - 15.8))

        # Resultado
        if(índice >= 16):
            print('Grade 16+')
        elif(índice < 1):
            print('Before Grade 1')
        else:
            print('Grade', índice)
        break
