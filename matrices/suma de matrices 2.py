filas = int(input ("Introduzca el numero de filas de sus matrices: "))
columnas = int(input ("Introduzca el numero de columnas de sus matrices: "))
A = []
B = []
S = []
for i in range (filas):
	A.append( [0] * columnas)
	B.append( [0] * columnas)
	S.append( [0] * columnas)
print ('Ingrese su Matriz 1')
for i in range(filas):
		for j in range(columnas):
			A[i][j] = float(input('Elemento (%d,%d): ' % (i, j)))
print ('Ingrese su Matriz 2')
for i in range(filas):
	for j in range(columnas):
			B[i][j] = float(input('Elemento (%d,%d): ' % (i, j)))

for i in range(filas):
	for j in range(columnas):
			S[i][j] += A[i][j] + B[i][j]
print ('Su matriz resultante es')
print (S)
