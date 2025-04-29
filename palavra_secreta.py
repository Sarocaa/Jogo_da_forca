import random  

lista_palavras = ['cereja', 'melancia', 'abacaxi', 'laranja', 'pitanga', 'morango', 
    'banana', 'ameixa', 'goiaba', 'graviola','damasco', 'acerola',
    'tamarindo', 'espinafre', 'alface', 'cenoura', 'ervilha', 'beterraba', 'mandioca', 
    'batatas', 'chuchu', 'jabuticaba']
palavra_secreta = random.choice(lista_palavras)

letras_corretas = ''
letras_tentadas = ''
tentativas = 0

print('Tente adivinhar a palavra secreta em no máximo 15 tentativas.\n' \
    'Como jogar: \n' \
    '- Digite somente letras (números, símbolos e espaços vão usar suas tentativas!);\n' \
    '- Digite apenas uma letra por vez (escrever mais de uma também vai usar suas tentativas!);\n' \
    '- Você tem 15 chances, boa sorte!')

while True :
    
    palavra_formada = ''

    if tentativas == 15 and palavra_formada != palavra_secreta:
        print(f'Você não acertou a palavra secreta. A palavra era {palavra_secreta}.')
        break

    letra = input('Digite uma letra: ')
    letra = letra.lower()
    tentativas += 1

    if len(letra) > 1 :
        print('Digite somente UMA letra.')
        continue

    if letra.isalpha() == False :
        print('Digite SOMENTE letras.')
        continue

    if letra in letras_tentadas:
        print('Você já tentou essa letra!')
        continue
        
    if letra not in palavra_secreta :
        letras_tentadas += letra

    if letra in palavra_secreta :
        letras_corretas += letra
        letras_tentadas += letra

    letras_unicas = sorted(set(letras_tentadas))
    letras_formatadas = ', '.join(letras_unicas)

    for letra_secreta in palavra_secreta :
        if letra_secreta in letras_corretas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    if palavra_formada == palavra_secreta:
        print(f'Você acertou a palavra "{palavra_secreta}" em {tentativas} tentativas. Parabéns!')
        break

    print(f'A palavra formada até agora é: {palavra_formada} \nVocê já tentou as letras: {letras_formatadas}')
