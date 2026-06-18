## 1. Mensaje de bienvenida
Crear una función que muestre *Bienvenido al sistema*. 
Mostrar este mensaje 3 veces.

```python
def saludar():
	print('Bienvenido al sistema')

for i in range(0,3):
	saludar()
```

## 2. Encabezado reutilizable
Crear una función que muestre el siguiente formato: 
```
--------------------
REGISTRO DE CLIENTES
--------------------
```
Invocarlo 2 veces.
## 3. Menú principal
Crear una función que muestre: 
```
1. Alta
2. Baja
3. Modificacion
4. Salir
```
Invocarla 1 vez.
## 4. Reporte de empleados
Crear una función que muestre: 
```
REPORTE DE EMPLEADOS
```
y debajo una lista fija de 3 empleados utilizando una lista.
La lista debe recorrerse dentro de la función.
## 5. Desafío integrador
Crear dos funciones:
1. Debe mostrar:
	```
	1. Registrar venta
	2. Ver venta
	3. Salir
	```
2. Debe mostrar
```
Sistema desarrollado en Python
```
Luego construir un programa principal que llame a ambas funciones.
## Razonamiento
Sin ejecutar nada: 
```python
def mensaje():
    print('Hola')

print('Inicio')

mensaje()

mensaje()

print('Fin')
```
Preguntas:
1. ¿Qué imprime el programa?
2. ¿Cuántas veces se ejecuta la función?
3. ¿En qué momento se ejecuta realmente el código dentro de `mensaje()`?
4. ¿Cuál es la diferencia entre:
```python
def mensaje():
```
y
```python
mensaje()
```
