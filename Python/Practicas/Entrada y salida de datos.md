1. Realizar un programa que pida nombre, apellido y ciudad y luego muestre:
	`Hola [nombre] [apellido], veo que eres de [ciudad]`
	
```python
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
ciudad = input("Ingrese su ciudad: ")

print(f'Hola {nombre} {apellido}, veo que eres de {ciudad}')
```

2. Realizar un programa que solicite nombre, edad y altura, y luego imprima todo en una sola linea usando `print`, `sep`,`end`.
```python
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
altura = float(input("Ingrese su altura: "))

print(f'Nombre: {nombre} - Edad: {edad} - Altura: {altura}')
```