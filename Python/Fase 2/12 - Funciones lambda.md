## 1. Calculadora de comisión
Una inmobiliaria necesita calcular la comisión de sus vendedores.
1. Solicitar el monto de una venta
2. La comisión es del 8% sobre el importe vendido
3. Muestra:
	- importe de venta
	- comisión obtenida

```python
venta = float(input('Ingrese el monto de venta: $'))  
  
comision = lambda x: x * 0.08  
  
print(f'Venta: ${venta:.2f}\n'  
      f'Comision: ${comision(venta):.2f}\n')
```

---
## 2. Verificación de acceso
En un edificio corporativo solo pueden ingresar empleados mayores de 21 anos.
1. Solicitar nombre y edad
2. Determinar si puede ingresar
3. Muestra un mensaje indicando el resultado

```python
def pedir_datos():  
    nombre = input("Ingrese nombre: ")  
    edad = int(input("Ingrese edad: "))  
    return nombre, edad  
  
def control_acceso(nombre,verificacion,edad):  
    if verificacion(edad):  
        return f'Puede ingresar'  
    else:  
        return f'No puede ingresar'  
  
nombre, edad = pedir_datos()  
verificacion_ing = lambda edad: edad > 21  
resultado = control_acceso(nombre,verificacion_ing,edad)  
  
print(resultado)
```

---
## 3. Catálogo de productos
Crea una lista con varias diccionarios, donde muestre el nombre y el precio con IVA incluido (21%).

```python
lista_productos = []  
  
def mostrar_menu():  
    opcion = int(input(f'1. Cargar producto\n'  
                       f'2. Mostrar listado de productos\n'  
                       f'0. Salir\n'  
                       f'Seleccione una opcion: '))  
    return opcion  
# ---  
def pedir_datos():  
    nombre = input('Ingrese el nombre del producto: ')  
    precio = float(input('Ingrese el precio del producto: $'))  
    return nombre, precio  
# ---  
def crear_producto(nombre,precio):  
    producto = {}  
  
    producto['nombre'] = nombre  
    producto['precio'] = precio  
  
    iva = lambda x: precio * 0.21  
    precio_iva = lambda x: precio + iva(x)  
  
    producto['iva'] = iva(precio_iva)  
    producto['precio_iva'] = precio_iva(precio_iva)  
  
    return producto  
# ---  
def mostrar_productos(lista):  
    for i in range(len(lista)):  
        print(f'{i+1}. {lista[i]['nombre'].upper()}\n'  
              f'- Precio: ${lista[i]['precio']}\n'  
              f'- IVA: ${lista[i]['iva']}\n'  
              f'- Precio + IVA: ${lista[i]['precio_iva']}\n')  
    print('Fin del listado...')  
  
opcion = 1  
  
while opcion != 0:  
    opcion = mostrar_menu()  
    if opcion == 1:  
        nombre,precio = pedir_datos()  
        producto = crear_producto(nombre,precio)  
        lista_productos.append(producto)  
        print(f'Producto cargado...')  
    elif opcion == 2:  
        mostrar_productos(lista_productos)  
    elif opcion == 0:  
        print('Saliendo del sistema...')  
        break
```

---
## 4. Gestión de descuentos
Registra varios productos (nombre y precio):
Luego muestra para cada uno:
- nombre
- precio original
- precio con un descuento del 15%

```python
lista_productos = []  
  
def mostrar_menu():  
    opcion = int(input(f'1. Cargar producto\n'  
                       f'2. Mostrar listado de productos\n'  
                       f'0. Salir\n'  
                       f'Seleccione una opcion: '))  
    return opcion  
# ---  
def pedir_datos():  
    nombre = input('Ingrese el nombre del producto: ')  
    precio = float(input('Ingrese el precio del producto: $'))  
    return nombre, precio  
# ---  
def crear_producto(nombre,precio):  
    producto = {}  
  
    producto['nombre'] = nombre  
    producto['precio'] = precio  
  
    des_15 = lambda x: precio * 0.15  
    precio_des = lambda x: precio - des_15(x)  
  
    producto['descuento'] = des_15(precio)  
    producto['precio_des'] = precio_des(precio)  
  
    return producto  
# ---  
def mostrar_productos(lista):  
    for i in range(len(lista)):  
        print(f'{i+1}. {lista[i]['nombre'].upper()}\n'  
              f'- Precio: ${lista[i]['precio']}\n'  
              f'- Descuento 25%: ${lista[i]['descuento']}\n'  
              f'- Precio con descuento: ${lista[i]['precio_des']}\n')  
    print('Fin del listado...')  
  
opcion = 1  
  
while opcion != 0:  
    opcion = mostrar_menu()  
    if opcion == 1:  
        nombre,precio = pedir_datos()  
        producto = crear_producto(nombre,precio)  
        lista_productos.append(producto)  
        print(f'Producto cargado...')  
    elif opcion == 2:  
        mostrar_productos(lista_productos)  
    elif opcion == 0:  
        print('Saliendo del sistema...')  
        break
```

---
## 5. Registro de empleados
Crea una lista con empleados.
Cada empleado tendrá:
- nombre
- salario
Al mostrar la información, indica además si el salario supera los $1.000.000

```python
TOPE = 1000000  
  
lista_empleados = []  
  
def mostrar_menu():  
    opcion = int(input(f'1. Cargar empleado\n'  
                       f'2. Mostrar listado de empleados\n'  
                       f'0. Salir\n'  
                       f'Seleccione una opcion: '))  
    return opcion  
# ---  
def pedir_datos():  
    nombre = input('Ingrese su nombre: ').capitalize()  
    salario = float(input('Ingrese su salario: $'))  
    return nombre, salario  
# ---  
def crear_empleado(nombre,salario,aux):  
    empleado = {}  
  
    empleado['nombre'] = nombre  
    empleado['salario'] = salario  
  
    verificacion_1m = lambda x: salario > aux  
  
    empleado['verificacion'] = verificacion_1m(salario)  
  
    return empleado  
# ---  
def mostrar_empleados(lista):  
    for i in range(len(lista)):  
        print(f'{i+1}. {lista[i]['nombre']}\n'  
              f'- Salario: ${lista[i]['salario']}\n'  
              f'- Supera el millon: {lista[i]['verificacion']}\n')  
    print('Fin del listado...')  
  
opcion = 1  
  
while opcion != 0:  
    opcion = mostrar_menu()  
    if opcion == 1:  
        nombre,salario = pedir_datos()  
        empleado = crear_empleado(nombre,salario,TOPE)  
        lista_empleados.append(empleado)  
        print(f'Empleado cargado...')  
    elif opcion == 2:  
        mostrar_empleados(lista_empleados)  
    elif opcion == 0:  
        print('Saliendo del sistema...')  
        break
```

---
## Desafío de razonamiento
Sin ejecutar el código.
```python
doble = lambda x: x * 2

print(doble(6))

triple = lambda x: x * 3

resultado = triple(doble(5))

print(resultado)
```
Responde:
1. ¿Qué imprime la primera llamada a `print()`?
	El primer `print()` imprime el resultado de la variable doble, que tiene asignado una función lambda.
2. ¿Qué valor devuelve `doble(5)`?
	Devuelve el valor de la función lambda asignada a esta variable, el cual es 10
3. ¿Qué recibe como parámetro la función `triple()`?
	`triple()` recibe como parámetro el resultado de la función lambda asignada a la variable `doble`
4. ¿Qué imprime el segundo `print()`?
	El segundo `print` imprime el valor de la variable `triple`, la cual tiene asignada una función lambda, que a su vez recibe como parámetro otra variable que tiene asignada una función lambda.
5. ¿Qué ventaja tiene poder guardar una función lambda en una variable?
	Que podemos guardar el resultado de esta función.