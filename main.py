
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


