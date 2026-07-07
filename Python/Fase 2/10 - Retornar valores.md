## 1. Calculo de facturación
Una empresa registra la cantidad vendida y el precio unitario de un producto.
Construir una función que realice el calculo correspondiente y permita la reutilizarla para distintas ventas.
Luego registrar 5 ventas y mostrar el total de cada una.

> [!quote|borde] Estado
> - [x] Completado

```python
def mostrar_menu(opcion,aux):  
  opcion = input(f'..:: MENU :..\n'  
                 f'{aux}\n'  
                 f'1. Cargar venta\n'  
                 f'2. Mostrar total de ventas\n'  
                 f'0. Salir\n'  
                 f'{aux}\n'  
                 f'Seleccione una opcion: ')  
  return int(opcion)  
  
def cargar_venta(lista,aux):  
  venta = {}  
  print(f'..:: CARGAR UNA VENTA ::..\n{aux}')  
  
  cantidad = int(input('Ingrese la cantidad de ventas: '))  
  precio_unitario = float(input('Ingrese la precio unitario: $'))  
  
  venta['cantidad'] = cantidad  
  venta['precio_unitario'] = precio_unitario  
  venta['total'] = cantidad * precio_unitario  
  
  lista.append(venta)  
  print(f'{aux}\n'  
        f'Producto cargado...\n'  
        f'{aux}\n')  
  
def mostrar_venta(lista,aux):  
  print(f'..:: MOSTRAR VENTA ::..\n{aux}')  
  print(f'-- cantidad de ventas realizadas: {len(lista)} --\n{aux}')  
  for i in range(len(lista)):  
    print(f'- Venta {i + 1}: {lista[i]["cantidad"]} productos')  
  print(aux)  
  opcion = int(input('Seleccione una opcion: '))  
  
  for i in range(len(lista)):  
    if opcion - 1 == i:  
      print(f'{aux}\nVenta: {i + 1}\n'  
            f'{aux}\n'  
            f'- Cantidad: {lista[i]["cantidad"]}\n'  
            f'- Precio unitario: ${lista[i]["precio_unitario"]}\n'  
            f'- Total: ${lista[i]["total"]:.2f}\n')  
  
list_ventas = []  
  
# variables  
deco = '-' * 25  
opcion = 1  
  
while opcion != 0:  
  opcion = mostrar_menu(opcion,deco)  
  print()  
  
  if opcion == 1:  
    cargar_venta(list_ventas,deco)  
  elif opcion == 2:  
    mostrar_venta(list_ventas,deco)  
  elif opcion == 0:  
    print('Saliendo del sistema...')  
    break  
  else:  
    print('Opcion invalida.')
```

## 2. Control de acceso
Crear una función que determine si una persona puede ingresar a un evento.
Reglas:
- debe ser mayor o igual a 18 años
- debe poseer entrada
Probar la función con varios casos.
>[!quote|borde] Estado
>- [x] Completado


```python
def puede_ingresar(edad,entrada):  
  if edad >= 18 and entrada == True:  
    ingresar = True  
  else:  
    ingresar = False  
  
  if ingresar == True:  
    return print('Puede ingresar')  
  else:  
    return print('No puede ingresar')  
  
def pedir_edad(edad,entrada):  
  edad = int(input("Ingrese su edad: "))  
  entrada = input("Posee entrada (si/no)? ").upper()  
  if entrada == "SI":  
    entrada = True  
  elif entrada == "NO":  
    entrada = False  
  else:  
    print('Dato ingresado invalido...')  
  return edad,entrada  
  
  
#variables  
edad = 0  
entrada = False  
  
edad, entrada = pedir_edad(edad,entrada)  
  
resultado = puede_ingresar(edad,entrada)
```

## 3. Análisis de temperaturas
Registrar temperaturas de varios días.
Construir una función que permita obtener el promedio de una colección de temperaturas.
Mostrar el resultado final.
>[!quote|borde] Estado
>- [x] Completado

```python
def mostrar_menu(opcion,aux):  
  opcion = int(input(f'..:: MENU ::..\n'  
                     f'{aux}\n'  
                     f'1. Cargar temperaturas del dia\n'  
                     f'2. Mostrar promedio de un dia\n'  
                     f'0. Salir\n'  
                     f'{aux}\n'  
                     f'Seleccione una opcion: '))  
  return opcion  
  
def cargar_temperatura(lista,aux,contador):  
  print(f'Cargar temperaturas del dia {contador}\n{aux}')  
  temperatura = {}  
  
  dato = float(input('Ingrese el valor del temperatura: '))  
  
  temperatura['valor'] = dato  
  
  
  
  lista.append(temperatura)  
  print(f'{aux}\n'  
        f'Dato cargado...\n')  
  
def cargar_otro_dia(dia,aux):  
  opcion = int(input(f'Desea cargar otro dato perteneciente al dia {dia}?\n'  
                 f'1. Si\n'  
                 f'2. No\n'  
                 f'{aux}\n'  
                 f'Seleccione una opcion: '))  
  if opcion == 1:  
    opcion = False  
    return opcion  
  elif opcion == 2:  
    opcion = True  
    return opcion  
  
def mostrar_listado_dias(lista,aux):  
  for i in lista:  
    print(f'{lista[i]['valor']}')  
  print(f'..:: Listado de dias ::..\n'  
        f'{aux}\n')  
  for i in range(len(lista)):  
    cantidad = len(lista[i])  
    print(f'- Dia {i + 1}: {cantidad}\n')  
  
# ---  
  
list_dias_temperaturas = []  
  
# ---  
# variables  
deco = '-' * 30  
contador_dia = 0  
opcion = 1  
  
while opcion != 0:  
  opcion = mostrar_menu(opcion,deco)  
  if opcion == 1:  
    cargar_dia = False  
    contador_dia += 1  
    while not cargar_dia:  
      cargar_temperatura(list_dias_temperaturas,deco,contador_dia)  
      cargar_dia = cargar_otro_dia(contador_dia,deco)  
  if opcion == 2:  
    mostrar_listado_dias(list_dias_temperaturas,deco)
```


```python
# version2
def mostrar_menu(opcion,aux):  
  opcion = int(input(f'..:: MENU ::..\n'    
                     f'{aux}\n'    
                     f'1. Cargar temperaturas\n'    
                     f'2. Mostrar promedio\n'    
                     f'0. Salir\n'    
                     f'{aux}\n'    
                     f'Seleccione una opcion: '))  
  return opcion  
  
def pedir_cantidad_dias(aux):  
  print(f'..:: CARGAR TEMPERATURAS ::..\n{aux}')  
  can_dias = int(input('Ingrese la cantidad de dias que va a registrar: '))  
  print(aux)  
  return can_dias  
  
def cargar_temperaturas(lista,dias,aux):  
  for i in range(dias):  
    dato = float(input(f'Ingrese la temperatura del dia {i + 1}: '))  
    lista.append(dato)  
  print(f'{aux}\nDatos cargados...\n{aux}')  
  
def mostrar_promedio(lista,aux):  
  suma = 0  
  print(f'..:: MOSTRAR PROMEDIO ::..\n{aux}')  
  for i in range(len(lista)):  
    suma += lista[i]  
  promedio = suma / len(lista)  
  return print(f'El promedio es: {promedio:.2f}')  
  
# lista  
lista_dias_temperatura = []  
  
  
# variables  
deco = '-' * 25  
contador_dia = 0  
opcion = 1  
  
while opcion != 0:  
  opcion = mostrar_menu(opcion,deco) # ✔  
  if opcion == 1:  
    dias = pedir_cantidad_dias(deco)  
    cargar_temperaturas(lista_dias_temperatura,dias,deco)  
    mostrar_promedio(lista_dias_temperatura,deco)  
  elif opcion == 0:  
    print(f'{deco}\nSaliendo del sistema..\n{deco}')  
    break  
  else:  
    print(f'{deco}\nValor ingresado no valido!\n{deco}')
```

## 4. Registro de empleados
Crear una función que reciba:
- nombre
- apellido
- sector
y genere la estructura de datos correspondiente para representar un empleado.
Registrar varios empleados utilizando esa función.
Finalmente mostrar el listado completo.

```python
def mostrar_menu(opcion,aux):  
  opcion = int(input(f'..:: MENU ::..\n'      
                     f'{aux}\n'      
                     f'1. Cargar empleado\n'      
                     f'2. Mostrar lista de empleados\n'      
                     f'0. Salir\n'      
                     f'{aux}\n'      
                     f'Seleccione una opcion: '))  
  return opcion  
  
def cargar_empleado(lista,aux):  
  print(f'{aux}\n..:: CARGAR EMPLEADO ::..\n{aux}')  
  salir = False  
  contador = 0  
  while not salir :  
    empleado = {}  
    contador += 1  
    print(f'Datos empleado {contador}\n{aux}')  
  
    nombre = input('Ingrese nombre del empleado: ').capitalize()  
    apellido = input('Ingrese apellido del empleado: ').capitalize()  
    sector = input('Ingrese sector de trabajo: ').capitalize()  
  
    empleado['nombre'] = nombre  
    empleado['apellido'] = apellido  
    empleado['sector'] = sector  
  
    lista.append(empleado)  
    print(f'{aux}\nDatos cargados...\n{aux}')  
  
    opcion = int(input(f'Cargar otro empleado ?\n'  
                       f'1. Si\n'  
                       f'2. No\n'  
                       f'{aux}\n'  
                       f'Seleccione una opcion: '))  
    print(aux)  
  
  
    if opcion == 2:  
      salir = True  
      break  
def mostrar_lista_empleados(lista,aux):  
  print(f'{aux}\n..:: MOSTRAR LISTA EMPLEADOS ::..\n{aux}\n'  
        f'-- cantidad total de empleados: {len(lista)} --\n{aux}')  
  for i in range(len(lista)):  
    print(f'DATOS EMPLEADO {i + 1}\n{aux}')  
    print(f'- Nombre: {lista[i]["nombre"]}\n'  
          f'- Apellido: {lista[i]["apellido"]}\n'  
          f'- Sector: {lista[i]["sector"]}\n{aux}')  
  
  
# lista  
lista_empleados = []  
  
# variables  
deco = '-' * 25  
opcion = 1  
  
while opcion != 0:  
  opcion = mostrar_menu(opcion,deco)  
  
  if opcion == 1:  
    cargar_empleado(lista_empleados,deco)  
  elif opcion == 2:  
    mostrar_lista_empleados(lista_empleados,deco)  
  elif opcion == 0:  
    print(f'{deco}\nSaliendo del sistema...\n{deco}')  
  else:  
    print(f'{deco}\nValor incorrecto...\n{deco}')
```

## 5. Resumen comercial
Registrar productos vendidos.
Para cada producto almacenar:
- nombre
- precio unitario
- cantidad
Utilizar funciones para:
- generar la información de cada producto
- calcular el importe total de cada venta
Al finalizar mostrar:
- listado de productos vendidos
- importe total por producto
- facturación general

```python
def mostrar_menu(aux):  
  opcion = int(input(f'..:: MENU ::..\n'        
                     f'{aux}\n'        
                     f'1. Cargar producto\n'        
                     f'2. Mostrar listado de productos\n'        
                     f'3. Mostrar importe total por producto\n'  
                     f'4. Mostrar factura general\n'  
                     f'0. Salir\n'        
                     f'{aux}\n'        
                     f'Seleccione una opcion: '))  
  return opcion  
  
def cargar_producto(lista,aux):  
  print(f'..:: CARGAR PRODUCTO ::..\n{aux}\n'  
        f'-- productos cargados: {len(lista)} --\n{aux}')  
  
  opcion = 1  
  
  while opcion == 1:  
    producto = {}  
  
    nombre = input('Ingrese el nombre del producto: ').capitalize()  
    cantidad = int(input('Ingrese la cantidad de producto: '))  
    precio = float(input('Ingrese el precio del producto: '))  
    imp_total = cantidad * precio  
  
    producto['nombre'] = nombre  
    producto['cantidad'] = cantidad  
    producto['precio'] = precio  
    producto['total'] = imp_total  
  
    lista.append(producto)  
    print(f'Producto cargado exitosamente!\n'  
          f'{aux}')  
    opcion = int(input(f'Cargar otro producto ?\n'  
                       f'1. Si\n'  
                       f'0. No\n'  
                       f'{aux}\n'  
                       f'Seleccione una opcion: '))  
  
def mostrar_list_prod_vendidos(lista,aux):  
  print(f'..:: LISTADO DE PRODUCTOS VENDIDOS ::..\n{aux}')  
  for i in range(len(lista)):  
    print(f'-- PRODUCTO - {i + 1} --\n'  
          f'- Nombre: {lista[i]["nombre"]}\n'  
          f'- Cantidad: {lista[i]["cantidad"]}\n{aux}')  
  print(f'-- fin listado de productos vendidos --\n{aux}\n')  
  
def mostrar_imp_total_prod(lista,aux):  
  print(f'..:: IMPORTE TOTAL POR PRODUCTO ::..\n{aux}')  
  for i in range(len(lista)):  
    print(f'-- PRODUCTO - {i + 1} --\n'  
          f'- Nombre: {lista[i]["nombre"]}\n'  
          f'- Cantidad: {lista[i]["cantidad"]}\n{aux}\n'  
          f'IMPORTE TOTAL: ${lista[i]["total"]:.2f}\n{aux}')  
  print(f'-- fin listado de productos vendidos --\n{aux}\n')  
  
def factura_general(lista,aux):  
  print(f'..:: FACTURA GENERAL ::..\n{aux}')  
  imp_total = 0  
  for i in range(len(lista)):  
    imp_total += lista[i]["total"]  
  
  print(f'Cantidad de productos: {len(lista)}\n{aux}\n'  
        f'TOTAL: ${imp_total:.2f}\n{aux}')  
lista_productos = []  
  
# variables  
deco = '-' * 25  
opcion = 0  
  
while True:  
  opcion = mostrar_menu(deco)  
  
  if opcion == 1:  
    cargar_producto(lista_productos,deco)  
  elif opcion == 2:  
    mostrar_list_prod_vendidos(lista_productos,deco)  
  elif opcion == 3:  
    mostrar_imp_total_prod(lista_productos,deco)  
  elif opcion == 4:  
    factura_general(lista_productos,deco)  
  elif opcion == 0:  
    print(f'Saliendo del sistema...')  
    break
```

## Desafío de razonamiento
Sin ejecutar:
```python
def calcular(a, b):
    return a + b

resultado = calcular(10, 20)

print(resultado)
```
Preguntas:
1. ¿Qué valor devuelve la función?
	La función devuelve el resultado de la operación a + b
2. ¿Qué valor queda almacenado en `resultado`?
	El valor que devuelve la función, en este caso la suma de los parámetros que se le pasa.
3. ¿Qué imprime el programa?
	El programa imprime 30.
4. ¿Qué ocurriría si reemplazáramos `return a + b` por `print(a + b)`?
	Se generara un erro porque no podemos asignar un print a una variable, ya que el codigo indica que se esta cargando lo que devuelva la función a la variable resultado.
5. ¿Cuál es la diferencia conceptual entre mostrar un dato y devolver un dato?
	Mostrar un dato es simplemente eso mostrarlo, no se puede realizar ningún tipo de manipulación sobre este mas que visual, devolver un dato implica que se puede utilizar este valor para cualquier operación que se requiera y además también mostrarlo.

---
## 1. Calcular descuento
Una tienda ofrece un **15% de descuento** sobre el precio de un producto.
Debes crear las funciones necesarias para que el programa:
1. Solicite al usuario el precio original del producto.
2. Calcule el precio final con el descuento.
3. Muestre el resultado al usuario.
>[!info|borde] Condición importante
>La función encargada del cálculo **no debe mostrar nada por pantalla**. Su única responsabilidad es realizar el cálculo y entregar el resultado.
>Piensa qué función debería usar `return` y cuál debería usar `print()`.

```python
def soli_precio():  
  precio = float(input("Ingrese el precio de la compra: $"))  
  return precio  
  
def descuento_15(precio):  
  calc_des = precio * 0.15  
  return calc_des  
  
def precio_final(precio,descuento):  
  calc_des = precio - descuento  
  return calc_des  
  
def mostrar_datos(precio,descuento,total,aux):  
  print(f'Importe: ${precio:.2f}\n'  
        f'Descuento 15%: ${descuento:.2f}\n'  
        f'{aux}\n'  
        f'Importe total: ${total:.2f}\n')  
  
  
deco = '-' * 25  
  
print(f'..:: CALCULADORA DE DESCUENTO ::..\n{deco}')  
precio = soli_precio()  
descuento = descuento_15(precio)  
total = precio_final(precio,descuento)  
mostrar_datos(precio,descuento,total,deco)
```

## 2. Clasificación de notas
Una academia necesita clasificar a sus alumnos según la nota obtenida.
Reglas:
- 7 o más → **Aprobado**
- Menor a 7 → **Desaprobado**
El programa debe:
1. Solicitar una nota.
2. Obtener la clasificación.
3. Mostrar el resultado.
>[!info|borde] Condición importante
>La función que decide si el alumno aprobó o desaprobó **no debe imprimir el texto**. Debe entregar el resultado para que otra parte del programa decida qué hacer con él.

```python
def solicitar_nota():  
  nota = float(input('Ingrese su nota (0-10): '))  
  return nota  
  
def clasificar_nota(nota):  
  if nota >= 0 and nota <= 10:  
    if nota >=0 and nota < 6:  
      return 'Desaprobado'  
    elif nota >= 6 and nota < 10:  
      return 'Aprobado'  
  else:  
    return 'ERROR: dato fuera de rango!'  
  
deco = '-' * 25  
  
print(f'..:: CLASIFICADOR DE NOTAS ::..\n{deco}')  
nota = solicitar_nota()  
resultado = clasificar_nota(nota)  
print(f'Resultado: {resultado}')
```

## 3. Registro de productos
Una tienda quiere registrar varios productos.
De cada uno se conoce:
- nombre
- precio
- stock
Debes construir una función que reciba esos datos y **genere el diccionario correspondiente**.
Luego:
- guardar cada producto en una lista;
- al finalizar, mostrar el listado completo.
>[!info|borde] Condición importante
>La función que crea el producto **no debe agregarlo a la lista ni mostrar mensajes**. Debe limitarse a construir el diccionario y devolverlo.

```python
def crear_producto(nombre, precio, stock):
    producto = {}

    producto['nombre'] = nombre
    producto['precio'] = precio
    producto['stock'] = stock

    return producto

def cargar_producto(producto, lista):
    lista.append(producto)
    print('Producto cargado...')

def pedir_datos():
    nombre = input('Nombre producto: ')
    precio = float(input('Precio: $'))
    stock = int(input('Cantidad: '))

    return nombre,precio,stock

def mostrar_productos(lista):
    for i in range(len(lista)):
        print(f'{i + 1}. {lista[i]['nombre']}\n'
              f'- Cantidad: {lista[i]['stock']}\n'
              f'- Precio: ${lista[i]['precio']:.2f}\n')

lista_producto = []

opcion = 1

while True:

    if opcion == 1:
        nombre, precio, stock = pedir_datos()
        producto = crear_producto(nombre, precio, stock)
        cargar_producto(producto, lista_producto)
    else:
        mostrar_productos(lista_producto)
        break
    opcion = int(input(f'Cargar nuevo producto ?\n'
                       f'1. Si\n'
                       f'0. No\n'
                       f'Seleccione una opcion: '))
```

## Razonamiento
Sin escribir código, responde únicamente con el concepto.
Imagina esta función:

```python
def calcular_promedio(notas):    
	promedio = sum(notas) / len(notas)    
	return promedio
```

Ahora responde:
1. ¿Por qué sería un mal diseño que esta función hiciera `print(promedio)` en lugar de `return promedio`?
	Porque en el caso de quere utilizar el dato de promedio con print solo podremos visualizarlo sin manipularlo, y en cambio return devuelve el valor numerico y lo podemos utilizar en otro procedimiento.
2. Menciona **dos situaciones distintas** en las que el valor devuelto podría reutilizarse sin modificar la función.
	Mostrar el promedio al usuario, asignando el valor a una variable.
	Utilizarlo en alguna operación donde se necesite el valor numérico de el resultado de la función.