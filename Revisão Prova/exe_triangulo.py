'''
Análise e Classificação de Triângulos
Autor(a): Dayane Dutra (1° Período - Técnico em Informática)
Última Modificação: 13/07/2026
Contato: dutra007@proton.me
'''

import math

def calcula_triangulo(a, b, c):

    '''
    Função que recebe como parâmetro 3 medidas de lados e verifica se formam um triângulo.
    Em caso positivo, calcula o perímetro e a área, classifica o triângulo em equilátero, escaleno ou isósceles
    e retorna "True" indicando que as medidas fornecidas formam um triângulo, o tipo de triângulo, o perímetro e a área.
    Em caso negativo, retorna "False" indicando que as medidas fornecidas não formam um triângulo e "None" para os demais valores.
    '''

    if a < b + c and b < a + c and c < a + b:

        perimetro = a + b + c
    
        semiperimetro = perimetro / 2

        area = math.sqrt(semiperimetro * (semiperimetro - a) * (semiperimetro - b) * (semiperimetro - c))

        if a == b == c:
            tipo = 'Equilátero'
        elif a != b != c:
            tipo = 'Escaleno'
        else:
            tipo = 'Isósceles'

        return True, tipo, perimetro, area

    else:
        return False, None, None, None

MAIOR_MEDIDA_INVALIDA = 0
PRIMEIRO_TRIANGULO_LIDO = 1
total_triangulos = 0
soma_perimetros = 0
soma_areas = 0
menor_perimetro_escaleno = None
maior_area_equilatero = None
menor_area_equilatero = None
total_isosceles = 0

lado1 = float(input('Forneça a medida do primeiro lado em metros (m): '))
lado2 = float(input('Forneça a medida do segundo lado em metros (m): '))
lado3 = float(input('Forneça a medida do terceiro lado em metros (m): '))

while lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print('Valores inválidos. As medidas dos lados devem ser maiores que 0 (zero).')
    lado1 = float(input('Forneça a medida do primeiro lado em metros (m): '))
    lado2 = float(input('Forneça a medida do segundo lado em metros (m): '))
    lado3 = float(input('Forneça a medida do terceiro lado em metros (m): '))

forma_triangulo, tipo_triangulo, perimetro, area = calcula_triangulo(lado1, lado2, lado3) 

while forma_triangulo == True:

    total_triangulos += 1

    soma_perimetros += perimetro

    soma_areas += area
        
    if tipo_triangulo == 'Escaleno':

        if menor_perimetro_escaleno is None:
            menor_perimetro_escaleno = perimetro
        elif perimetro < menor_perimetro_escaleno:
            menor_perimetro_escaleno = perimetro

    elif tipo_triangulo == 'Equilátero':

        if maior_area_equilatero is None:
            maior_area_equilatero = area
            menor_area_equilatero = area
        else:
            if area > maior_area_equilatero:
                maior_area_equilatero = area
                
            if area < menor_area_equilatero:
                menor_area_equilatero = area

    else:
        total_isosceles += 1

    print('--' * 50)

    lado1 = float(input('Forneça a medida do primeiro lado em metros (m): '))
    lado2 = float(input('Forneça a medida do segundo lado em metros (m): '))
    lado3 = float(input('Forneça a medida do terceiro lado em metros (m): '))

    while lado1 <= MAIOR_MEDIDA_INVALIDA or lado2 <= MAIOR_MEDIDA_INVALIDA or lado3 <= MAIOR_MEDIDA_INVALIDA:
        print('Valores inválidos. As medidas dos lados devem ser maiores que 0 (zero).')
        lado1 = float(input('Forneça a medida do primeiro lado em metros (m): '))
        lado2 = float(input('Forneça a medida do segundo lado em metros (m): '))
        lado3 = float(input('Forneça a medida do terceiro lado em metros (m): '))

    forma_triangulo, tipo_triangulo, perimetro, area = calcula_triangulo(lado1, lado2, lado3)

if total_triangulos >= PRIMEIRO_TRIANGULO_LIDO:
    print('--' * 50)

    if menor_perimetro_escaleno is not None:
        print(f'Menor Perímetro - Escaleno: {menor_perimetro_escaleno:.1f} m')
    else:
        print('Nenhum triângulo escaleno foi lido.')

    if maior_area_equilatero is not None:
        print(f'Maior Área - Equilátero: {maior_area_equilatero:.1f} m2\nMenor Área - Equilátero: {menor_area_equilatero:.1f} m2')
    else:
        print('Nenhum triângulo equilátero foi lido.')

    if total_isosceles >= 1:
        print(f'Total de Triângulos Isósceles: {total_isosceles}')
    else:
        print('Nenhum triângulo isósceles foi lido.')

    print(f'Média dos Perímetros: {soma_perimetros / total_triangulos:.1f} m')

    print(f'Soma das Áreas: {soma_areas:.1f} m2')

else:
    print('--' * 50)
    print('Nenhum triângulo foi lido.')
