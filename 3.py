# Faça um programa em Python que solicite ao usuário que digite uma frase. Este programa deverá inverter a ordem das palavras e apresentá-las na tela.

#Exemplo:
#Frase digitada: Programa Feito em Python
#Saída na tela: Python em Feito Programa


texto = input("Digite uma frase: ") 

palavras = texto.split(" ")
print(f"Frase invertida: {palavras[::-1]}")



