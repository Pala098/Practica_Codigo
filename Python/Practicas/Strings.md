1. Crear un programa que:
	- Solicite nombre y apellido
	- Convierta ambos a formato correcto
	- Muestre: 
		- Usuario registrado
		- Nombre completo
		- Cantidad de caracteres 

```python
name_user = input('Ingrese su nombre completo: ')

partes = name_user.split()

first_name = partes[0].strip().capitalize()
last_name = partes[1].strip().capitalize()

total_char = len(first_name) + len(last_name)

print(f'Usuario registrado: \nNombre: {first_name}\nApellido: {last_name}\nCantidad de caracteres: {total_char}')
```

2. Solicitar un corre electrónico.
	Determinar si contiene `@` y `.`. Si ambos existen:
	- Correo valido
	Caso contrario --> correo invalido.

```python
user_email = input('Ingrese su email: ')

if '@' in user_email and '.' in user_email:
    print('Email valido')
else:
    print('Email invalido')
```

3. Solicitar una palabra. Mostrar:
	- Primera letra
	- Ultima letra
	- Cantidad de caracteres

```python
user_txt = input('Ingrese una palabra: ')

for letra in range(len(user_txt)):
  if letra == 0:
    print(user_txt[0])
  if letra == len(user_txt) - 1:
    print(user_txt[letra])
print(f'Cantidad de caracteres: {len(user_txt.strip())}')
```

4. Solicitar una frase/ Luego solicitar una letra.
	Indicar:
	- si la letra existe en la frase
	- en que posición aparece por primera vez

```python
frase = input('Ingrese una frase: ').upper()
letra = input('Ingrese una letra: ').upper()

if letra in frase: 
	for i in range(len(frase)):
		if frase[i] == letra:
			print(f'Posicion: {frase[i]}:{i}')
else:
	print('No se encontro conincidencias.')
```

5. Una empresa desea registrar 3 empleados.
	Para cada empleado:
	- Solicita nombre
	- Convierte a formato correcto (`capitalize()`)
	Mostrar:
	
	```txt
	Empleado 1: nombre
	Empelado 2: nombre
	Empleado 3: nombre
	```

Y además indicar la cantidad total de caracteres almacenados entre todos los nombres.

```python
acumulador = 0
empleado = ''

for i in range(0,3):
	empleado = input(f'Ingrese su nombre empleado {i}: ').capitalize()
	
	acumulador += len(empleado)
	
	print(f'Empleado {i}: {empleado}')
print(f'Cantidad total de caracteres: {acumulador}')
```