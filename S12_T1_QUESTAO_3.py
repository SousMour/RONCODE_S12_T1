#Dado um país A, com taxa de natalidade de 2% ao ano, e um país B com uma taxa de natalidade de 3% ano. 
# Sabe-se que, atualmente, o país A tem população maior que o país B. 
# Faça um programa que leia a população de cada país 
# e imprima o tempo necessário para que a população do país B ultrapasse a população do país A.


pais_a = int(input())
pais_b = int(input())
tempo = 0
if pais_a < pais_b:
        pais_a , pais_b = pais_b , pais_a
        
while pais_a > pais_b:
    pais_a += pais_a * 0.02
    pais_b += pais_b * 0.03
    tempo += 1
print(tempo)