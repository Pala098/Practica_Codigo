1. Realizar un programa que:
	1. Solicite un numero
	2. Indique si:
		- Es positivo
		- negativo
		- o cero

```python
num1 = int(input('Ingrese un numero: '))

if num1 > 0:
	print('Positivo')
elif num1 < 0:
	print('negativo')
else:
	print('es cero')
```

2. Realizar un programa que:
	1. Solicite:
		- usuario
		- contraseña
	2. valide:
		- usuario "admin"
		- contraseña "python123"
	3. Muestre:
		- bienvenido
		- datos incorrectos

```python
USUARIO = 'admin'
CONTR = 'python123'

user = input('Ingrese su usuario: ')
password = input('Ingrese su contrasena: ')

if user == USUARIO and password == CONTR:
	print('Bienvenido')
else:
	print('Datos incorrectos')
```

3. Realizar un programa que solicite una nota del 1 al 10 e indique:
	- 9-10 --> excelente
	- 7-9 --> aprobado
	- 4-6 --> recuperatorio
	- 1-3 --> desaprobado

```python
nota = int(input('Ingrese su nota: '))

if nota >= 9 and nota <=10:
	print('Excelente')
elif nota < 9 and nota >= 7:
	print('Aprobado')
elif nota <= 6 and nota >=4:
	print('Recuperatorio')
else:
	print('Desaprobado')

```

4. Hacer un programa que solicite:
	- edad
	- tiene licencia (true o false)
	y determine si puede conducir.
	Condición:
	- debe ser mayor o igual a 18
	- y tener licencia

```python
edad = int(input('Ingrese su edad: '))
tiene_licencia = input('Tiene licencia ? (si/no)').upper()

if tiene_licencia == 'SI':
	tiene_licencia = True
elif tiene_licencia == 'NO':
	tiene_licencia = False
else: 
	print('Dato ingresado incorrecto')
	
if edad >= 18 and tiene_licencia:
	print('Cumple con los requisitos para conducir.')
elif edad <= 18 or tiene_licencia == False:
	print('No cumple con almenos uno de los requisitos para conducir.')
else: 
	print('No cumple con ningun requisito.')
```