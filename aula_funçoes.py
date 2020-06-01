def dobra(valor):
    for i in valor:
        print(f'2x{i} = {2 * i}')
    for j in range(0, len(valor)):
        valor[j] *= 2
    print(valor)


valores = [7, 2, 5, 0, 4]
dobra(valores)
