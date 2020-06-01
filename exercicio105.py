def notas(num, sit=False):
    """
    Função para calcular o total e a média de uma lista de alunos, imprimir no formato de
    dicionario; Parametro 'sit' = 'situação': caso o parametro 'sit' seja passado como True
    o dicionario irá receber a chave 'situação' e será impressa no dicionario;
    caso 'sit' = False, esse parametro sera ignorado
    :param num: lista ou tupla com os valores a serem calculados
    :param sit: (OPCIONAL) adiciona uma chava 'situação' os dicionario caso 'sit' = True
    :return: Um dicionario que informa o total de notas calculadas, a média das notas,
    maior e menor nota passada por parametro, e opcionalmente a 'situação'
    """
    soma = maior = menor = 0
    tamanho = len(num)
    for i in range(0, len(num)):
        if i == 0:
            maior = menor = num[i]
        if num[i] > maior:
            maior = num[i]
        if num[i] < menor:
            menor = num[i]
        soma += num[i]
    media = soma / len(num)
    resultado = {'total': tamanho, 'maior': maior, 'menor': menor, 'média': media}
    if sit == True:
        if media >= 6.5:
            resultado['situação'] = 'Boa'
        elif media < 6.5 and media >= 5:
            resultado['situação'] = 'Razoavél'
        else:
            resultado['situação'] = 'Ruim'
    print()
    print('-' * 30)
    for k, v in resultado.items():
        print(f'"{k}": {v}', end=' ')
    print()


listanotas = [5, 6.5, 10, 4, 8, 3, 7, 7.5, 9, 5, 6, 6, 7, 10, 5.6, 6.5, 4.5, 5.5, 9]
#notas(5, 4, 3.5, 5, 3, 4, 8, 2)
notas(listanotas, sit=True)
print('-=' * 15)
help(notas)
