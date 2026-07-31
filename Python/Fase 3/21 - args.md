## Ejercicio 1 — Caja del supermercado
Una caja registradora debe calcular el importe total de una compra.
La función debe poder recibir cualquier cantidad de importes.
Ejemplo de uso:

```
calcular_total(1200, 3500, 800, 250)
```

Debe devolver el total de la compra.

```python
def calcular_total(*compras):
    total = 0

    for compra in compras:
        total += compra
    return total

total_compras = calcular_total(1200, 3500, 800, 250)

print(total_compras)

```
---
## Ejercicio 2 — Asistencia a una capacitación
Crear una función que reciba el nombre del instructor y luego cualquier cantidad de nombres de asistentes.
La salida podría verse así:

```
Instructor: Carlos

Asistentes:

Ana
Pedro
María
Lucas
```

```python
def procesar_datos(instructor, *args):  
    print(f'Instructor: {instructor}\n')  
    print(f'Asistentes:\n')  
    for asistente in args:  
      print(f'{asistente}')  
  
datos_usuario = []  
  
instructor = input("Instructor: ")  
  
print("Ingresa datos (escribe 'fin' para terminar):")  
while True:  
    entrada = input("> ")  
    if entrada.lower() == 'fin':  
        break  
    datos_usuario.append(entrada)  
  
procesar_datos(instructor,*datos_usuario)
```
---

## Ejercicio 3 — Sistema de ventas
Crear una función que reciba el nombre del cliente y una cantidad variable de importes de compras.
Debe mostrar:
- cliente
- cantidad de compras
- total gastado
- promedio por compra

```python
def calcular_tota(*lista):  
  total = 0  
  for compra in lista:  
    total += compra  
  return total  
  
def calcular_promedio(*lista):  
  total = 0  
  for compra in lista:  
    total += compra  
  promedio = total/len(lista)  
  return promedio  
  
def procesar_datos(cliente, *compras):  
  deco = '-' * 25  
  print(f'Cliente: {cliente}\n'  
        f'{deco}')  
  print(f'- Cantidad de compras: {len(compras)}\n'  
        f'- Total gastado: ${total}\n'  
        f'- Promedio: {promedio}\n')  
  
lista_compras = []  
  
cliente = input("Cliente: ")  
  
print("Ingresa datos (escribe '0' para terminar):")  
while True:  
  entrada = float(input("> $"))  
  if entrada == 0:  
    break  
  lista_compras.append(entrada)  
  
total = calcular_tota(*lista_compras)  
  
promedio = calcular_promedio(*lista_compras)   
  
procesar_datos(cliente, *lista_compras,total,promedio)
```

> [!bug|borde] Corrección
> Acá aparece un detalle importante.
> Vos hiciste:
> ```python
> procesar_datos(cliente,
> 		   *lista_compras,
> 		   total,
> 		   promedio)
> ```
> Entonces dentro de la función:
> ```
> compras =
> (
> 1200,
> 800,
> 500,
> 2500,
> 5000,   ← total
> 1250    ← promedio
> )
> ```
> Es decir...
> **el total y el promedio también terminan formando parte de `*compras`.**
> No era la idea.
> Lo correcto sería:
> ```python
> def procesar_datos(cliente, *compras):
> ```
> y dentro calcular:
> ```python
> total = sum(compras)
> promedio = total / len(compras)
> ```
> Así la función es totalmente independiente.
> Ese concepto se llama:
> **función autocontenida**.
> Mientras menos dependa de variables externas, mejor diseñada está.
> **La solución funciona**, pero el diseño puede mejorar.

---
## Ejercicio 4 — Control de stock
Crear una función que reciba una cantidad variable de productos representados por diccionarios como:

```
{
    "nombre": "...",
    "stock": ...
}
```

La función debe indicar:
- cantidad de productos recibidos
- cuántos tienen stock
- cuántos están sin stock

```python
deco = "-" * 25  
  
lista_productos = []  
  
def mostrar_menu():  
  opcion = int(input(f'..:: MENU ::..\n'  
                     f'{deco}\n'  
                     f'1. Cargar producto\n'  
                     f'2. Mostrar productos con stock\n'  
                     f'3. Mostrar productos sin stock\n'  
                     f'0. Salir\n'  
                     f'{deco}\n'  
                     f'Seleccione una opcion: '))  
  
  return opcion  
  
def cargar_datos(lista):  
  producto = {}  
  
  producto["nombre"] = input("Ingrese el nombre del producto: ")  
  producto["stock"] = int(input("Ingrese el stock del producto: "))  
  
  if producto["stock"] == ' ' or producto["stock"] == None:  
    producto["stock"] = 0  
  
  lista.append(producto)  
  print("Producto cargado...")  
  print('\n')  
  
def mostrar_productos_con_stock(*lista):  
  producto_con_stock = 0  
  
  for producto in lista:  
    if producto["stock"] > 0:  
      producto_con_stock += 1  
  
  print(f'PRODUCTOS SIN STOCK: {producto_con_stock}\n')  
  
def mostrar_productos_sin_stock(*lista):  
  producto_sin_stock = 0  
  
  for producto in lista:  
    if producto["stock"] == 0:  
      producto_sin_stock += 1  
  
  print(f'PRODUCTOS SIN STOCK: {producto_sin_stock}\n')  
  
opcion = 1  
  
while opcion != 0:  
  opcion = mostrar_menu()  
  if opcion == 1:  
    cargar_datos(lista_productos)  
  elif opcion == 2:  
    mostrar_productos_con_stock(*lista_productos)  
  elif opcion == 3:  
    mostrar_productos_sin_stock(*lista_productos)  
  elif opcion == 0:  
    print(f'Saliendo del sistema...')  
    break  
  else:  
    print('Opcion no valida')
```
---
## Ejercicio 5 — Evaluación de empleados
Cada empleado estará representado por un diccionario:

```
{
    "nombre": "...",
    "salario": ...
}
```

La función debe recibir una cantidad variable de empleados y devolver:
- salario total
- salario promedio
- nombre del empleado con mayor salario
No utilices funciones como `max()` todavía; resolvelo recorriendo los datos.

```python
deco = "-" * 25  
  
lista_empleados = []  
  
def mostrar_menu():  
  opcion = int(input(f'..:: MENU ::..\n'  
                     f'{deco}\n'  
                     f'1. Cargar datos empleado\n'  
                     f'2. Mostrar salario total\n'  
                     f'3. Mostrar salario promedio\n'  
                     f'3. Nombre del empleado con mayor salario\n'  
                     f'0. Salir\n'  
                     f'{deco}\n'  
                     f'Seleccione una opcion: '))  
  
  return opcion  
  
def cargar_datos(lista):  
  empleado = {}  
  
  empleado["nombre"] = input("Ingrese nombre del empleado: ")  
  empleado["salario"] = float(input("Ingrese salario: $ "))  
  
  lista.append(empleado)  
  print("Empleado cargado...")  
  print()  
  
def mostrar_salario_total(*lista):  
  total_salario = 0  
  
  for empleado in lista:  
    total_salario += empleado["salario"]  
  
  print(f'Total de salario: ${total_salario}\n')  
  
def mostrar_salario_promedio(*lista):  
  total_salario = 0  
  
  for empleado in lista:  
    total_salario += empleado["salario"]  
  
  promedio = total_salario / len(lista)  
  
  print(f'Promedio de salario: ${promedio}\n')  
  
def mostrar_nombre_con_mayor_salario(*lista):  
  mayor_salario = -999  
  nombre = ''  
  
  for empleado in lista:  
    if empleado["salario"] > mayor_salario:  
      nombre = empleado["nombre"].upper()  
  
  print(f'Nombre del empleado con mayor salario: {nombre}')  
  
opcion = 1  
  
while opcion != 0:  
  opcion = mostrar_menu()  
  if opcion == 1:  
    cargar_datos(lista_empleados)  
  elif opcion == 2:  
    mostrar_salario_total(*lista_empleados)  
  elif opcion == 3:  
    mostrar_salario_promedio(*lista_empleados)  
  elif opcion == 4:  
    mostrar_nombre_con_mayor_salario(*lista_empleados)  
  elif opcion == 0:  
    print(f'Saliendo del sistema...')  
    break  
  else:  
    print('Opcion no valida')
```

>[!bug|borde] Corrección
>Todo muy bien excepto un pequeño bug.
>Hiciste:
>```python
>if empleado["salario"] > mayor_salario:
> 	nombre = empleado["nombre"]
>```
> Pero nunca actualizás
> ```
> mayor_salario
> ```
> Debería ser
> ```
> if empleado["salario"] > mayor_salario:
>     mayor_salario = empleado["salario"]
> 	nombre = empleado["nombre"]
> ```
> Si no, cada salario será mayor que -999 y terminará mostrando simplemente el último empleado.

---
# Desafío de razonamiento
Analizá el siguiente código sin ejecutarlo:

```
def mostrar(*datos):
    print(datos)

mostrar(10, 20)
mostrar("Ana")
mostrar()
```

Respondé:
1. ¿Qué contiene `datos` en la primera llamada?
	`datos` contendrá `(10,20)` en la primera llamada.
2. ¿Qué contiene en la segunda?
	Contiene `"Ana"` en la segunda.
3. ¿Qué contiene en la tercera?
	No contiene nada en la tercera.
4. ¿Por qué `datos` siempre es una tupla, incluso cuando no recibe argumentos?
	La verdad no se la respuesta.

> [!bug|borde] Corrección
> Acá estaba la única que faltó.
> ¿Por qué siempre es una tupla?
> Porque Python internamente hace esto.
> Cuando escribí
> ```python
> def mostrar(*datos):
> ```
> Python automáticamente convierte todos los argumentos posicionales en una tupla.
> Ejemplo:
> ```python
> mostrar(1,2,3)
> ```
> equivale internamente a
> ```python
> datos = (1,2,3)
> ```
> Y si llamás
> ```python
> mostrar()
> ```
> entonces
> ```python
> datos = ()
> ```
> Es decir, **siempre existe la tupla**, solamente que puede estar vacía.
> Por eso podés hacer
> ```python
> len(datos)
> ```
> sin importar cuántos argumentos llegaron.


5. ¿Qué ventaja aporta `*args` frente a definir una función con cinco parámetros fijos?
	La ventaja es que podemos tener parámetros variables, y englobar a cualquier numero con solo utilizar`*args`, porque este los agrupa.
