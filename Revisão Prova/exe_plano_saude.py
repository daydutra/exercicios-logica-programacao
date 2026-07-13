'''
Sistema de Orçamento de Planos de Saúde
Autor(a): Dayane Dutra (1° Período - Técnico em Informática)
Última Modificação: 13/07/2026
Contato: dutra007@proton.me
'''

def vita_saude(renda_mensal, idade, anos_contribuicao, numero_internacoes):
    PERCENTUAL_VALOR_BASE = 0.10
    IDADE_MAXIMA_ACRESCIMO = 30
    PERCENTUAL_AJUSTE_IDADE_ACRESCIMO = 0.02
    PERCENTUAL_MAXIMO_AJUSTE_IDADE_ACRESCIMO = 0.16
    IDADE_MINIMA_DESCONTO = 50
    PERCENTUAL_AJUSTE_IDADE_DESCONTO = 0.01
    PERCENTUAL_MAXIMO_AJUSTE_IDADE_DESCONTO = 0.15
    MINIMO_ANOS_CONTRIBUICAO = 3
    PERCENTUAL_DESCONTO_ANOS_CONTRIBUICAO = 0.05
    MINIMO_INTERNACOES = 2
    PERCENTUAL_ACRESCIMO_INTERNACOES = 0.2

    valor_base = renda_mensal * PERCENTUAL_VALOR_BASE

    valor_plano = valor_base

    if idade < IDADE_MAXIMA_ACRESCIMO:
        ajuste_idade = (IDADE_MAXIMA_ACRESCIMO - idade) * PERCENTUAL_AJUSTE_IDADE_ACRESCIMO

        if ajuste_idade > PERCENTUAL_MAXIMO_AJUSTE_IDADE_ACRESCIMO:
            ajuste_idade = PERCENTUAL_MAXIMO_AJUSTE_IDADE_ACRESCIMO

        valor_plano = valor_base + (valor_base * ajuste_idade)

    elif idade > IDADE_MINIMA_DESCONTO:
        ajuste_idade = (idade - IDADE_MINIMA_DESCONTO) * PERCENTUAL_AJUSTE_IDADE_DESCONTO

        if ajuste_idade > PERCENTUAL_MAXIMO_AJUSTE_IDADE_DESCONTO:
            ajuste_idade = PERCENTUAL_MAXIMO_AJUSTE_IDADE_DESCONTO

        valor_plano = valor_base - (valor_base * ajuste_idade)

    if anos_contribuicao > MINIMO_ANOS_CONTRIBUICAO:
        valor_plano = valor_plano - (valor_plano * PERCENTUAL_DESCONTO_ANOS_CONTRIBUICAO)
    
    if numero_internacoes > MINIMO_INTERNACOES:
        valor_plano = valor_plano + (valor_plano * PERCENTUAL_ACRESCIMO_INTERNACOES)

    return valor_plano

def omega_seguros(renda_mensal, sexo, idade, anos_contribuicao, numero_internacoes):
    PERCENTUAL_VALOR_BASE = 0.12
    CODIGO_SEXO_FEMININO = 1
    PERCENTUAL_DESCONTO_SEXO_FEMININO = 0.05
    IDADE_MINIMA_DESCONTO = 30
    PERCENTUAL_DESCONTO_IDADE = 0.1
    TEMPO_MINIMO_CONTRIBUICAO = 0
    PERCENTUAL_AJUSTE_IDADE = 0.03
    PERCENTUAL_MAXIMO_AJUSTE_IDADE = 0.15
    MINIMO_INTERNACOES = 0
    PERCENTUAL_DESCONTO_MINIMO_INTERNACOES = 0.1
    MAXIMO_INTERNACOES = 2
    total_percentual_desconto = 0
    cliente_inelegivel = False
    
    valor_base = renda_mensal * PERCENTUAL_VALOR_BASE

    valor_plano = valor_base

    if sexo == CODIGO_SEXO_FEMININO:
        total_percentual_desconto = PERCENTUAL_DESCONTO_SEXO_FEMININO
    
    if idade >= IDADE_MINIMA_DESCONTO:
        total_percentual_desconto += PERCENTUAL_DESCONTO_IDADE
    
    if anos_contribuicao > TEMPO_MINIMO_CONTRIBUICAO:
        ajuste_fidelidade = anos_contribuicao * PERCENTUAL_AJUSTE_IDADE

        if ajuste_fidelidade > PERCENTUAL_MAXIMO_AJUSTE_IDADE:
            ajuste_fidelidade = PERCENTUAL_MAXIMO_AJUSTE_IDADE
        
        total_percentual_desconto += ajuste_fidelidade
    
    valor_plano = valor_base - (valor_base * total_percentual_desconto)

    if numero_internacoes == MINIMO_INTERNACOES:
        valor_plano = valor_plano - (valor_plano * PERCENTUAL_DESCONTO_MINIMO_INTERNACOES)
    elif numero_internacoes <= MAXIMO_INTERNACOES:
        valor_plano = valor_plano
    else:
        cliente_inelegivel = True

    return valor_plano, cliente_inelegivel

PLATAFORMA = 'LifeCompare'
CODIGO_SEXO_FEMININO = 1
CODIGO_SEXO_MASCULINO = 2
IDADE_MINIMA_REQUERIDA = 18
IDADE_MAXIMA_REQUERIDA = 80
RENDA_MINIMA_REQUERIDA = 2000
TEMPO_MINIMO_CONTRIBUICAO = 0
NUMERO_MINIMO_INTERNACOES = 0
PRIMEIRO_CLIENTE_PROCESSADO = 1
PRIMEIRO_CLIENTE_ELEGIVEL_OMEGA = 1
total_clientes_processados = 0
total_clientes_inelegiveis_omega = 0
soma_valores_vita = 0
total_clientes_elegiveis_omega = 0
soma_valores_omega = 0
maior_valor_vita = None
menor_valor_vita = None
maior_valor_omega = None
menor_valor_omega = None

print('1 - Feminino\n2 - Masculino\nOutro Valor - Encerrar Programa')
sexo = int(input('Digite o código referente ao sexo do cliente ou outro valor para encerrar o programa: '))

while sexo == CODIGO_SEXO_FEMININO or sexo == CODIGO_SEXO_MASCULINO:

    idade = int(input('Digite a idade do cliente de 18 a 80 anos: '))

    while idade < IDADE_MINIMA_REQUERIDA or idade > IDADE_MAXIMA_REQUERIDA:
        print('Idade inválida. Digite um valor de 18 a 80.')
        idade = int(input('Digite a idade do cliente de 18 a 80 anos: '))

    renda_mensal = float(input('Digite a renda mensal do cliente (mínimo de R$ 2.000,00): '))

    while renda_mensal < RENDA_MINIMA_REQUERIDA:
        print('Renda Mensal inválida. Digite um valor maior ou igual a R$ 2.000,00.')
        renda_mensal = float(input('Digite a renda mensal do cliente (mínimo de R$ 2.000,00): '))

    anos_contribuicao = int(input(f'Digite o tempo em anos que o cliente possui outra apólice com a {PLATAFORMA}: '))

    while anos_contribuicao < TEMPO_MINIMO_CONTRIBUICAO:
        print('Tempo de Contribuição inválido. Digite um valor maior ou igual a 0 (zero).')
        anos_contribuicao = int(input(f'Digite o tempo em anos que o cliente possui outra apólice com a {PLATAFORMA}: '))
    
    numero_internacoes = int(input('Digite o número de internações hospitalares do cliente nos últimos 3 anos: '))

    while numero_internacoes < NUMERO_MINIMO_INTERNACOES:
        print('Número de Internações inválido. Digite um valor maior ou igual a 0 (zero).')
        numero_internacoes = int(input('Digite o número de internações hospitalares do cliente nos últimos 3 anos: '))

    valor_plano_vita = vita_saude(renda_mensal, idade, anos_contribuicao, numero_internacoes)

    valor_plano_omega, situacao_cliente = omega_seguros(renda_mensal, sexo, idade, anos_contribuicao, numero_internacoes)

    print('--' * 50)

    print(f'Plano VITA Saúde: R$ {valor_plano_vita:.2f}')
    
    if situacao_cliente == True:
        print('Plano OMEGA Seguros: Cliente inelegível')
        total_clientes_inelegiveis_omega += 1
    else:
        print(f'Plano OMEGA Seguros: R$ {valor_plano_omega:.2f}')
        total_clientes_elegiveis_omega += 1
        soma_valores_omega += valor_plano_omega

        if maior_valor_omega is None:
            maior_valor_omega = valor_plano_omega
            menor_valor_omega = valor_plano_omega
        else:
            if valor_plano_omega > maior_valor_omega:
                maior_valor_omega = valor_plano_omega
            if valor_plano_omega < menor_valor_omega:
                menor_valor_omega = valor_plano_omega
    
    print('--' * 50)

    total_clientes_processados += 1

    soma_valores_vita += valor_plano_vita

    if maior_valor_vita is None:
        maior_valor_vita = valor_plano_vita
        menor_valor_vita = valor_plano_vita
    else:
        if valor_plano_vita > maior_valor_vita:
            maior_valor_vita = valor_plano_vita
        if valor_plano_vita < menor_valor_vita:
            menor_valor_vita = valor_plano_vita

    print('1 - Feminino\n2 - Masculino\nOutro Valor - Encerrar Programa')
    sexo = int(input('Digite o código referente ao sexo do cliente ou outro valor para encerrar o programa: '))

if total_clientes_processados >= PRIMEIRO_CLIENTE_PROCESSADO:
    print('\n----- RELATÓRIO FINAL -----\n')
    print(f'Total de Clientes Processados: {total_clientes_processados}')
    print(f'Total de Clientes Inelegíveis na OMEGA Seguros: {total_clientes_inelegiveis_omega}')
    print(f'- VITA Saúde:\nMédia dos Valores: R$ {soma_valores_vita / total_clientes_processados:.2f}')
    print(f'Maior Valor Registrado: R$ {maior_valor_vita:.2f}')
    print(f'Menor Valor Registrado: R$ {menor_valor_vita:.2f}')

    if total_clientes_elegiveis_omega >= PRIMEIRO_CLIENTE_ELEGIVEL_OMEGA:
        print(f'- OMEGA Seguros:\nMédia dos Valores: R$ {soma_valores_omega / total_clientes_elegiveis_omega:.2f}')
        print(f'Maior Valor Registrado: R$ {maior_valor_omega:.2f}')
        print(f'Menor Valor Registrado: R$ {menor_valor_omega:.2f}')
    else:
        print('- OMEGA Seguros:\nNenhum valor válido foi processado.')
else:
    print('Programa Encerrado.')
