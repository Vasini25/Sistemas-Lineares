import math

n = int(input())
soma = 0

# Create zero matrix
A = [[0.0]*n for i in range(n)]
L = [[0.0]*n for i in range(n)]
Lt = [[0.0]*n for i in range(n)]
b = [0.0]*n
D = [0.0]*n
x = [1.0]*n
y = [0.0]*n

# For user input
for i in range(n):
    for j in range(i):
        A[i][j] = float(input())
        A[j][i] = A[i][j]
        L[i][j] = 1
        Lt[j][i] = 0

    A[i][i] = float(input())
    L[i][i] = 1
    Lt[i][i] = 1

for i in range(n):
	b[i] = (float(input()));

#Para Obter LDLT:

for i in range(n):
    for j in range(n):
        soma = 0;
        k = 1
        if (i == j):
            for k in range(j):
                soma += (L[j][k]*L[j][k])*D[k]
            D[i] = A[i][i] - soma
        elif (i > j):
            for k in range(j):
                soma += (L[i][k]*L[j][k]*D[k])
            L[i][j] = (A[i][j] - soma)/D[j]
        else:
            L[i][j] = 0

#Matriz A fatorada em LDLT

for i in range(n):               #Monta matriz Lt
    for j in range(n):
        Lt[i][j] = L[j][i]
        print("\nMatriz L:\n")
        print("%.6f" % L[i][j]);

'''Agora o método mais fácil para achar os valores do vetor das incógnitas
é transformando LDLT em LLT (ou HHT), ou seja, Cholesky '''

for i in range(n):
    for j in range(n):
        Lt[i][j] = Lt[i][j]*(math.sqrt(D[i]))
        L[j][i] = Lt[i][j]

for i in range(n):                #Resolve Hy = b
    for j in range(i):
        b[i] = b[i]-(y[j]*L[i][j])
    y[i] = b[i]/L[i][i]

i = n-1

while(i>=0):
    j = n-1                            #Resolve HTx = y
    while(j>i):
        y[i] = y[i] - (x[j]*Lt[i][j])
        j = j-1
    x[i] = y[i] / Lt[i][i]
    i = i-1

print("\nMatriz H:\n")
for i in range(n):
	for j in range(n):
		print("%.6f" % L[i][j]);

print("\nDiagonal da matriz D:\n")
for i in range(n):
	print("%.6f" % D[i]);

print("\nVetor Solução:\n")
for i in range(n):
	print("%.6f" % x[i]);