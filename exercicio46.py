from time import sleep

for n in range(10, -1, -1):
    print(n)
    sleep(1)
print('\033[7mFeliz ANO NOVO!!\033[m')