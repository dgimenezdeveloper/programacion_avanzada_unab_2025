Ejercicio 1:

a) Dado el siguiente código indique cuáles son los parámetros reales y los formales:
```python
#Definición de funciones
def sumaAlcuadrado(x, y):
    rta = x**2 + 2*x*y + y**2
    return rta
```
```python
#Programa principal
print (“Bienvenidos/as a la Suma al Cuadrado”)
a=input(“Ingrese el valor de a:”)
b=input(“Ingrese el valor de b:”)
print (sumaAlcuadrado(a, b))
```
Los parámetros reales son a y b, los parámetros formales son x e y.

b)Mencione los errores en los siguientes códigos. Justifique:

a) 
```python
def suma(par1, par2):
    print(par1+par2)
suma()
```
El error es que la función suma espera dos parámetros 
y no se le pasan ninguno.
b) 
```python
def suma(par1, par2):
    print (par1 + par2)
    print(suma(12, 10))
```
El error es que la función suma no retorna ningún valor,
por lo que no se puede imprimir.

c) 
```python
def suma(par1, par2):
    return (par1 + par2)

suma(12, 10)
```
El error es que la función suma retorna un valor pero no se imprime.

d) 
```python
def suma(par1):
    return (par1 + 2)
suma(12, 10)
```
El error es que la función suma espera un solo parámetro y se le pasan dos.