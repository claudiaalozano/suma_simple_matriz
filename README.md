# suma_simple_matriz
Mi link de Github es: https://github.com/claudiaalozano/suma_simple_matriz.git

A continuación muestro un esquema de cómo sería el código para este programa:
![figma suma matriz](https://user-images.githubusercontent.com/91722847/146638633-05ee22d7-73a8-4753-9d44-80eb73c1a7c7.png)

El código finalmente es:
```from random import randint


numero_filas = int(input("Seleccione el número de filas de la matriz: "))
numero_columnas = int(input("Seleccione el número de columnas de la matriz: "))

matriz = []
for i in range(numero_filas):
    matriz.append([])
    for j in range(numero_columnas):
        matriz[i].append(int(randint(0,100)))

suma = 0 

for i in range(numero_filas):
    for j in range(numero_columnas):
        suma = suma + matriz[i][j]
        suma = int(suma)

for i in range (numero_filas):
    print(matriz[i])

print(suma)
```
