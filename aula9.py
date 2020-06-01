frase = 'Curso em Video Python'
print(frase[9])

frase = 'Curso em Video Python'
print(frase[9:13])

frase = 'Curso em Video Python'
print(frase[9:21])

frase = 'Curso em Video Python'
print(frase[9:21:2]) #pula de 2 em 2

frase = 'Curso em Video Python'
print(frase[:5])

frase = 'Curso em Video Python'
print(frase[15:])

frase = 'Curso em Video Python'
print(frase[9::2]) # pula de 2 em 2 sem final definido

# MANIPULAÇÃO DE STRINGS

#Analise
len(frase)
# frase.count('o') conta quantas vezes tem a str 'o'
# frase.count('o':0:13) conta a str 'o' fatiada
# frase.find('deo') mostra a posição que começa o valor informado
# frase.find('Android') se a str não existe ele retorna -1 (não econtrado)
# 'Curso' in frase mostra se existe 'Curso' em frase

# Transformação

# frase.replace('Python','Android') Substitui uma str pela outra
# frase.upper() transforma o case sensitivi para maisculo
# frase.lower() transforma o case sensitivi para minusculo
# frase.capitalize() Só o primeiro caractere se mantem maiuscula
# frase.title() Mantém o inicio em maisculo baseado nos espaçoes (palavra por palavra)
# frase.strip() remove espaçoes inuteis no começo e no final da string
# frase.rstrip() remove espaços inuteis somente a direita
# frase.lstrip() remove espações inuteis somente a esquerda

# Divisão

# frase.split() dividi a string baseada nos espaçoes/gera uma lista com todas as plavras de uma cadeia de caracteres
# '-'.join(frase) junta o que foi feito no split