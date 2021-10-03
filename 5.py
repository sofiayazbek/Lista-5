#  Faça um programa em Python que leia uma String de dados da seguinte forma:
#nome=Robson,email=robson.luz@fae.edu;nome=Joao,email=joao@email.com

#E apresente para o usuário da seguinte forma:

#Usuários cadastrados: 2
#==============================================
#Usuário 1
#Nome: Robson
#E-mail: robson.luz@fae.edu
#==============================================
#Usuário 2
#Nome: Joao
#E-mail: joao@email.com
#============================================== 


import random

x = " "
y = " "
nomes = []
emails = []
#usuario = []

while True :
  for i in range(len(x)):
    x = input("Digite seu nome: ")
    nomes.append(x)
    y = input("Digite seu e-mail: ")
    emails.append(y)

    #usuario = [i]
    nome = x
    email = y


    print("==============================")
    print(f"Usuário: {i} ")
    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print("==============================")












