#O dodô é uma ave não voadora, extinta atualmente, e que era endêmica da Ilha Maurítius, na costa leste da África. 
# A partir do ano 1600, durante cada ano, 6% dos animais dos animais vivos no começo do ano morreram 
# e o número de animais nascidos ao longo do ano que sobreviveram foi de 1% da população inicial.
# Escreva um programa que leia a população de aves no início do ano 1600 
# e imprime, anualmente, a partir do fim de 1600, 
# o número de nascimentos, mortes e o total da população por ano (apenas a parte inteira do números, separados por vírgula). 
# O programa encerra sua execução quanto a população total cai para menos de 10% da população original.

pop_inicial = int(input())
ano_inicial = 1600
populacao_atual  = pop_inicial 
while populacao_atual >= 0.1 * pop_inicial:
    nascido = populacao_atual * 0.01
    mortos = populacao_atual * 0.06
    populacao_atual = populacao_atual - mortos + nascido
    print(ano_inicial, round(nascido),round(mortos),round(populacao_atual),sep=',')
    ano_inicial += 1