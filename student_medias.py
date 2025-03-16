# Um programa que peça o número de estudantes e o número de notas de cada um
# Irá permitir escrever as notas de cada aluno
# Irá calcular a médio de cada um

print("+--------------------------------+")
print("|        MÉDIA DE ALUNOS         |")
print("+--------------------------------+")
amoutStudents = int(input("| 1 - Digite quantos alunos são: "))
amoutNotes = int(input("| 2 - Digite quantas notas são para cada aluno: "))
print("+--------------------------------+")

totalNotes = 0
totalMedias = []
for i in range(int(amoutStudents)):
  for j in range (int(amoutNotes)):
    totalNotes += int(input(f"Digite nota {j+1} do estudante {i+1}: "))
  
  totalMedias.append(totalNotes/amoutNotes)
  totalNotes = 0

for i in range (len(totalMedias)):
  print(f"A média do estudante {i} é {totalMedias[i]}")


