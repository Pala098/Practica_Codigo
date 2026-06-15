1. Hacer un programa que imprima los números del 1 -> 10.

```python
contador = 0

while contador < 11: # --> correccion contador <= 10
	contador += 1
	print(contador)
```

2. Hacer un programa que imprima los números del 10 -> 1.

```python
contador = 10

while contador >= 1:
	contador -= 1 # -> print(contador)
	print(contador) # -> contador -= 1
```

3. Hacer un programa que solicite un numero, mientras el usuario ingrese un numero negativo, vuelva a pedirlo y cuando ingrese un numero positivo muestre `Numero valido`.

```python
numero = int(input('Ingrese un numero: '))

while numero < 0:
	numero = int(input('Ingrese un numero: '))
print('Numero valido')
```

4. Hacer un programa que pida 5 números, los vaya sumando y al final muestre su total

```python
contador = 1
acumulador = 0


while contador <= 5:
	dato_usuario = int(input('Ingrese un numero: '))
	acumulador += dato_usuario
	contador += 1
print(f'Suma total: {acumulador}')
```