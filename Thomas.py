# " Entrada: "
# " n - dimensao da matriz A e do sistema linear Ax=b "
# " d0 - entradas da diagonal principal da matriz SPD tridiagonal "
# " d1 - entradas da diagonal inferior (e superior ja que simetrica) "
# " b - vetor lado-direito do sistema Ax=b "


n = int(input())

# Create zero matrix
d0 = [0] * n
d1 = [0] * (n - 1)
d2 = [0] * (n - 1)
b = [0] * n
x = [0] * n

for i in range(n):
    d0[i] = float(input());

for i in range(n - 1):
    d1[i] = float(input());

for i in range(n - 1):
    d2[i] = float(input());

for i in range(n):
    b[i] = float(input());

# " Neste ponto, n, A e b sao conhecidos. Voce deve adicionar o "
# " seu codigo que resolva o sistema Ax=b atraves do algoritmo de"
# " Thomas."

for i in range(n-1):
    if(i==0):
        d2[i] = d2[i]/d0[i];
    else:
        d2[i] = d2[i]/(d0[i] - d2[i-1]*d1[i-1]);

i=0;

while (i<n):
    if(i==0):
        b[i] = b[i]/d0[i]
        i = i+1;
    else:
        b[i] = (b[i] - b[i-1]*d1[i-1])/(d0[i] - d2[i-1]*d1[i-1])
        i = i+1;

i = n-1;


while(i>=0):
    if(i==n-1):
        x[i] = b[i]
        #x[i] = x[i] * (-1);
        i = i-1;
    else:
        x[i] = b[i] - (d2[i]*x[i+1])
        #x[i] = x[i]*(-1);
        i = i-1;


for i in range(n):
    #print(x[i]);
    print("%.6f" % x[i]);