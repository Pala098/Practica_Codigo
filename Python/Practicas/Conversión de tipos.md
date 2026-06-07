1. Realizar un programa que solicite dos números esteros, los convierta correctamente y muestre:
	- Suma
	- Resta
	- Multiplicación
```python
num_1 = int(input("Ingrese el primer numero: "))
num_2 = int(input("Ingrese el segundo numero: "))

suma = num_1 + num_2
resta = num_1 - num_2
producto = num_1 * num_2

print(f'Numeros ingresados: {num_1},{num_2}')
print(f'Suma: {suma} - Resta: {resta} - Multiplicacion: {producto}')
```
2. Hacer un programa que solicite nombre, edad, salario mensual, convierta los tipos correctamente y muestre:
	Empleado: {nombre}
	Edad: {edad}
	Salario: ${salario}
```python
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
salario = float(input("Ingrese su salario: "))

print(f'Empleado: {nombre}/nEdad: {edad} /nSalario: ${salario:.1f}')
```
Corrección
```python
print(f'Empleado: {nombre}\nEdad: {edad}\nSalario: ${salario:.1f}')
```
3. Investigar que ocurre en el siguiente código:
```python
bool("")
bool(" ")
bool(0)
bool(1)
bool(-5)
```
Lo ocurrido es que se convierte el tipo de dato, donde las tres primeras toman un valor de `false` y las ultimas dos toman el valor de `true`