from random import randint

caracteres = ['0', '1']
camada_y = camada_x = 0
limite_x = camada_x + 2
camada = ''
limite_y = 4

print(f'{caracteres[randint(0, 1)]:^51}')

while limite_x <= 10:
    while camada_y < limite_y:
        while camada_x <= limite_x:
            camada += caracteres[randint(0, 1)]
            camada_x += 1

        print(f"{camada:^51}")
        camada = ''

        camada_x = 0
        limite_x += 2
        camada_y += 1

    camada_y = 0
    camada_x -= 6
    limite_x -= 6
    limite_y += 2

for i in range(3):
    for i in range(4):
        camada += caracteres[randint(0, 1)]

    print(f"{camada:^51}")
    camada = ''
