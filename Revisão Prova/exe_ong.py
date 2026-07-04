'''
Sistema de Triagem do Centro de Resgate Ambiental
Autor(a): Dayane
Última Modificação: 03/07/2026
Contato: dayane@gmail.com
'''

CODIGO_AVE = 1
CODIGO_REPTIL = 2
CODIGO_PEQUENO_MAMIFERO = 3
CODIGO_ONCA_PARDA = 4
CODIGO_URGENCIA_BAIXO = 1
CODIGO_URGENCIA_MEDIO = 2
CODIGO_URGENCIA_ALTO = 3
PRIMEIRA_OCORRENCIA_REGISTRADA = 1
total_carlos = 0
total_amanda = 0
total_renato = 0
total_ave = 0
total_reptil = 0
total_pequeno_mamifero = 0
total_onca_parda = 0
total_baixo = 0
total_medio = 0
total_alto = 0

print('1 - Ave\n2 - Réptil\n3 - Pequeno Mamífero\n4 - Onça-Parda\nOutro Valor - Encerrar Programa\n')
tipo_animal = int(input('Digite o código referente ao tipo de animal a ser resgatado: '))

while tipo_animal >= CODIGO_AVE and tipo_animal <= CODIGO_ONCA_PARDA:

    if tipo_animal == CODIGO_AVE:
        total_ave += 1
    elif tipo_animal == CODIGO_REPTIL:
        total_reptil += 1
    elif tipo_animal == CODIGO_PEQUENO_MAMIFERO:
        total_pequeno_mamifero += 1
    else:
        total_onca_parda += 1
        total_alto += 1
        total_renato += 1

    if tipo_animal != CODIGO_ONCA_PARDA:
        print('1 - Baixo\n2 - Médio\n3 - Alto\n')
        nivel_urgencia = int(input('Digite o código referente ao nível de urgência do atendimento: '))
        
        while nivel_urgencia < CODIGO_URGENCIA_BAIXO or nivel_urgencia > CODIGO_URGENCIA_ALTO:
            print('Cógido inválido. Forneça um número dentre as opções disponíveis.')
            print('1 - Baixo\n2 - Médio\n3 - Alto\n')
            nivel_urgencia = int(input('Digite o código referente ao nível de urgência do atendimento: '))
    
        if nivel_urgencia == CODIGO_URGENCIA_BAIXO:
            total_baixo += 1
        elif nivel_urgencia == CODIGO_URGENCIA_MEDIO:
            total_medio += 1
        else:
            total_alto += 1

        if total_carlos <= total_amanda and total_carlos <= total_renato:
            total_carlos += 1
        elif total_amanda <= total_renato:
            total_amanda += 1
        else:
            total_renato += 1
    
    print('--' * 50)
    print(f'Total de Atendimentos\nDr. Carlos: {total_carlos}\nDra. Amanda: {total_amanda}\nDr. Renato: {total_renato}')
    print('--' * 50)
    
    print('1 - Ave\n2 - Réptil\n3 - Pequeno Mamífero\n4 - Onça-Parda\nOutro Valor - Encerrar Programa\n')
    tipo_animal = int(input('Digite o código referente ao tipo de animal: '))

if total_carlos >= PRIMEIRA_OCORRENCIA_REGISTRADA or total_amanda >= PRIMEIRA_OCORRENCIA_REGISTRADA or total_renato >= PRIMEIRA_OCORRENCIA_REGISTRADA:
    print(f'\n----- RELATÓRIO FINAL -----\n')
    print(f'Total de Ocorrências - Tipo de Animal\nAve: {total_ave}\nRéptil: {total_reptil}\nPequeno Mamífero: {total_pequeno_mamifero}\nOnça-Parda: {total_onca_parda}\n')
    print(f'Total de Ocorrências - Nível de Urgência\nBaixo: {total_baixo}\nMédio: {total_medio}\nAlto: {total_alto}')
else:
    print('\nPrograma encerrado.')
