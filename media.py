#!/usr/bin/env python3

# Este script é para fazer o cálculo da média ponderada.

# Variáveis que iram receber suas notas
A1 = float(input('Informe a nota da A1: '))
A2 = float(input('Informe a nota da A2: '))
A3 = float(input('Informe a nota da A3: '))

# A1 possui peso 30, A2 possui peso 30 e A3 possui peso 40.
# P é a soma dos pesos de cada avaliação.
P = 100

# Calcula a média ponderada
media = ((A1 * 30) + (A2 * 30) + (A3 * 40)) / P

# Imprimi o resultado
if media >= 70:
    print ('Aprovado com média: ', media)
else:
    print ('Reprovado com média: ', media)
