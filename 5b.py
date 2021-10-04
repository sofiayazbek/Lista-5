texto = "nome=Robson,email=robson.luz@fae.edu;nome=Joao,email=joao@email.com"

registros = texto.split(";")

print(f"Usuários cadastrados: {len(registros)}")
print("====================")
for registro in registros:
  campos = registro.split(",")
  for campo in campos:
    valores = campo.split("=")
    print(f"{valores[0].capitalize()}: {valores[1]}")
  print("====================")
