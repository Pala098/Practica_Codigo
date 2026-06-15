1. Realizar un programa que solicite dos números y muestre:
	- suma
	- división
	- división entera
	- modulo
	- potencia del primer numero elevado al segundo

```python
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

operacion = num1 + num2
print(f'Suma: {operacion}')

operacion = num1 / num2
print(f'Division: {operacion}')

operacion = num1 // num2
print(f'Division entera: {operacion}')

operacion = num1 % num2
print(f'Modulo: {operacion}')

operacion = num1 ** num2
print(f'Potencia: {operacion}')
```

2. Realizar un programa que solicite una edad, que determine:
	- si es mayor de edad
	- si es menor edad
	Imprimir los resultados booleanos.

```python
edad = int(input('Ingrese su edad: '))
print(f'Edad: {edad}\nMayor de edad: {edad >= 18}')
```

3. Realizar un programa que solicite una palabra y determine:
	- si contiene la letra "a"
	- si contiene la letra "z"

```python
txt1 = input('Ingrese una palabra: ')

print('a' in txt1)
print('z' in txt1)
```

4. Que resultado producen estas expresiones y explciar su por que.
	- `10 > 5 and 3 < 1`
		Resultado: True, porque ambas condiciones se cumplen
	- `10 > 5 or 3 < 1`
		Resultado: True, porque una condicion si se cumple, y basta con que una sea true para que devuelva true
	- `not(10 > 5)`
		Originalmente devuelve true, pero al aplicar el not devuelve Flase ya que este lo niega
	 