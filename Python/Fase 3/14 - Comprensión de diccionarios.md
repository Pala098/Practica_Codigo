## Ejercicio #1 - Catálogo de productos
Disponés de la siguiente lista:

```
productos = [
    "Mouse",
    "Teclado",
    "Monitor",
    "Notebook",
    "Auriculares"
]
```

Generá un diccionario donde:
- la clave sea el nombre del producto;
- el valor sea `0`, representando el stock inicial.
Luego mostrá el diccionario completo.

```python
productos = [  
    "Mouse",  
    "Teclado",  
    "Monitor",  
    "Notebook",  
    "Auriculares"  
]  
  
lista_productos = {  
  producto : 0  
  for producto in productos  
}  
  
print(lista_productos)
```
---
## Ejercicio #2 - Ajuste salarial
Disponés del siguiente diccionario:

```
salarios = {
    "Ana": 850000,
    "Juan": 1200000,
    "María": 980000,
    "Pedro": 1500000
}
```

La empresa otorgó un aumento del **12%** a todos los empleados.
Generá un nuevo diccionario con los salarios actualizados y luego mostralo.

```python
salarios = {  
    "Ana": 850000,  
    "Juan": 1200000,  
    "María": 980000,  
    "Pedro": 1500000  
}  
  
salarios_act = {  
  empleado : salario * 1.12  
  for empleado, salario in salarios.items()  
}  
print(salarios_act)
```
---
## Ejercicio #3
Disponés de esta lista:

```
productos = [
    {"nombre": "Mouse", "stock": 12},
    {"nombre": "Monitor", "stock": 0},
    {"nombre": "Teclado", "stock": 5},
    {"nombre": "Notebook", "stock": 2},
    {"nombre": "Auriculares", "stock": 0}
]
```

Construí un diccionario donde:
- la clave sea el nombre del producto;
- el valor sea el stock;
- solo se incluyan los productos que tienen stock mayor que cero.
Finalmente, mostrá el resultado.

```python
productos = [  
    {"nombre": "Mouse", "stock": 12},  
    {"nombre": "Monitor", "stock": 0},  
    {"nombre": "Teclado", "stock": 5},  
    {"nombre": "Notebook", "stock": 2},  
    {"nombre": "Auriculares", "stock": 0}  
]  
  
lista_nue_productos = {  
  producto['nombre'] : producto['stock']  
  for producto in productos  
  if producto['stock'] > 0  
}  
  
print(lista_nue_productos)
```
---
## Ejercicio #4
Solicitá al usuario los datos de **5 personas**:
- nombre;
- número de teléfono.
Al finalizar la carga, construí un diccionario donde el nombre sea la clave y el teléfono el valor.
Luego mostrá toda la agenda.

```python
def pedir_datos():  
  nombre = input('Ingrese el nombre: ')  
  telefono = input('Ingrese el telefone: ')  
  return nombre, telefono  
  
  
contador = 0  
lista = []  
  
  
while contador < 5:  
  nombre, telefono = pedir_datos()  
  contador += 1  
  valor = {nombre: telefono}  
  lista.append(valor)  
  
print(lista)
```
---
## Ejercicio #5
Una empresa posee la siguiente información:

```
inventario = [
    {"producto": "Mouse", "cantidad": 25},
    {"producto": "Monitor", "cantidad": 8},
    {"producto": "Notebook", "cantidad": 3},
    {"producto": "Auriculares", "cantidad": 40},
    {"producto": "Teclado", "cantidad": 15}
]
```

Creá un nuevo diccionario donde:
- la clave sea el nombre del producto;
- el valor indique si debe realizarse una reposición (`True` o `False`).
Un producto necesita reposición cuando su cantidad es **menor a 10**.
Mostrá el diccionario obtenido.

```python
inventario = [  
    {"producto": "Mouse", "cantidad": 25},  
    {"producto": "Monitor", "cantidad": 8},  
    {"producto": "Notebook", "cantidad": 3},  
    {"producto": "Auriculares", "cantidad": 40},  
    {"producto": "Teclado", "cantidad": 15}  
]  
  
lista_repo = {  
  producto['producto'] : producto['cantidad'] < 10  
  for producto in inventario  
}  
  
print(lista_repo)
```
---
## Desafío de razonamiento
Analizá el siguiente código **sin ejecutarlo**:

``` python
productos = {
    "Mouse": 15000,
    "Teclado": 28000,
    "Monitor": 220000,
    "Auriculares": 18000
}

resultado = {
    producto: precio
    for producto, precio in productos.items()
    if precio < 50000
}

print(resultado)
```

Respondé:
1. ¿Qué elementos recorre la comprensión del diccionario?
	`for producto, precio in productos.items()`
2. ¿Qué condición deben cumplir para formar parte del nuevo diccionario?
	`if precio < 50000`
3. ¿Qué claves tendrá el diccionario `resultado`?
	Las claves que tendrá serán los nombres de los productos, y si es por el resultado los valores que cumplan con la condición (que son 'Mouse', 'Teclado' y 'Auriculares').
4. ¿Qué valores estarán asociados a esas claves?
	El valor numérico, que es el precio correspondiente a cada producto.
5. ¿Qué diferencia principal existe entre una **List Comprehension** y una **Dictionary Comprehension**?
	En si su función es básicamente es la misma, la única diferencia que encuentro es que una crea una lista y la otra un diccionario, el cual nos permite guardar los datos en formato clave - valor.