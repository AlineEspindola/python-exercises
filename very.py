# Faça um vetor que mostre os números dele multiplicados por um número de entrada

vector = [5, 2, 6, 10]

multiplier = float(input("Digite o multiplicador: "))

for i in range(len(vector)):
    vector[i] = round(vector[i]*multiplier)

print("vector: ", (vector))



# Crie uma função que receba uma lista de números e retorne a soma de todos os seus elementos.
running = True
numbers = []
while running:
    number = int(input("Digite o valor do número: "))
    continueRunning = input("Digite S para escrever outro número ou N para encerrar: ")
    numbers.append(number)
    if continueRunning == "N":
        running = False

sum = 0
for number in numbers:
    sum += number

print("A soma dos valores digitados é: ", sum)




matrix = [
    [1, 6],
    [4, 7],
    [1, 8]
]

totalCriminals = 0
totalCriminalsAux = 0
districtCriminals = []
for district in matrix:
    for criminals in district:
        totalCriminals += criminals
        totalCriminalsAux += criminals
    districtCriminals.append(totalCriminalsAux)
    totalCriminalsAux = 0

print("O total de criminosos: ", totalCriminals)
for i in range(len(districtCriminals)):
    print(f"O bairro {i+1} tem {districtCriminals[i]}")







# Crie uma função que verifique se duas matrizes são iguais (mesmo número de linhas, colunas e mesmos elementos correspondentes).

matrix1 = [
    [2, 2, 2,],
    [2, 2, 2],
    [2, 2, 2],
]

matrix2 = [
    [2, 2, 2],
    [2, 2, 2],
    [2, 2, 2]
]

def compareMatrices(matrix1, matrix2):
    if len(matrix1) == len(matrix2):
        for i in range(len(matrix1)):
            if matrix1[i] != matrix2[i]:
                return False
        return True
    return False

if compareMatrices(matrix1, matrix2):
    print("São iguais")
else:
    print("Não são iguais")



phrase = input("Escreva uma frase: ")

count = len(phrase)-1
result = ""
print("count: ", count)

while count >= 0:
    result += phrase[count]
    count -= 1

print("A frase invertida: ", result)





number = int(input("Digite um número para verificar se é primo: "))
primeNumber = True 
for i in range(2, number):
    if number%i == 0:
        primeNumber = False

if primeNumber:
    print("É número primo")
else:
    print("Não é número primo")
        


# Faça uma matriz em forma coordenadas, onde cada casa demostra o número de cachorros. Diga a maior quantidade de cachorros existente

dogs = (
    (5, 102),
    (1, 19)
)

biggerDog = 0
for line in dogs:
    for dog in line:
        if biggerDog < dog:
            biggerDog = dog

print(biggerDog)



matrix = [
    [5, 1, 100],
    [7, 810, 900]
]

bigger = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if bigger < matrix[i][j]:
            bigger = matrix[i][j]
            line = i
            column = j

print(f"Linha {line + 1} e coluna {column + 1}")
