## 1. Control de caja
Un comercio desea registrar el dinero disponible en caja.
El programa debe permitir:
- mostrar el saldo actual
- registrar un ingreso de dinero
- registrar el egreso de dinero
- finalizar el programa

```python
dinero_en_caja = 0 # --> var global  
  
def mostrar_menu(opcion):  
  opcion = int(input(f'..:: MENU ::..\n'  
                     f'1. Mostrar saldo\n'  
                     f'2. Ingresar dinero\n'  
                     f'3. Sacar dinero\n'  
                     f'0. Salir\n'  
                     f'Ingrese una opcion: '))  
  
  return opcion  
  
def mostrar_saldo(total_en_caja):  
  print(f'Saldo en caja: ${total_en_caja}')  
  
def ingresar_dinero(total_en_caja):  
  monto_ing = float(input('Digite la cantidad a ingresar: $'))  
  total_dinero = total_en_caja + monto_ing  
  return total_dinero  
  
def sacar_dinero(total_dinero):  
  monto_ext = float(input('Digite la cantidad a extraer: $'))  
  total_dinero = total_dinero - monto_ext  
  return total_dinero  
  
opcion = 1  
  
while opcion != 0:  
  opcion = mostrar_menu(opcion)  
  if opcion == 1:  
    mostrar_saldo(dinero_en_caja)  
  elif opcion == 2:  
    dinero_en_caja = ingresar_dinero(dinero_en_caja)  
  elif opcion == 3:  
    dinero_en_caja = sacar_dinero(dinero_en_caja)  
  elif opcion == 0:  
    print('Saliendo...')  
    break
```

---
## 2. Registro de empleados
Construye un programa que permita registrar empleados.
Cada empleado debe almacenar:
- nombre
- apellido
- sector
- salario
El sistema debe permitir:
- agregar empleados
- mostrar el listado completo
- consultar el salario promedio

```python
lista_empleados = []  
  
def pedir_datos():  
  nombre = input("Ingrese nombre: ").capitalize()  
  apellido = input("Ingrese apellido: ").upper()  
  sector = input("Ingrese sector: ").capitalize()  
  salario = float(input("Ingrese salario: $"))  
  
  return nombre, apellido, sector, salario  
  
def crear_empleado(nombre,apellido,sector,salario):  
  empleado = {}  
  
  empleado["nombre"] = nombre  
  empleado["apellido"] = apellido  
  empleado["sector"] = sector  
  empleado["salario"] = salario  
  
  return empleado  
  
def cargar_empleado(lista,empleado):  
  lista.append(empleado)  
  print(f'Empleado cargado...!')  
  
def mostrar_lista(lista):  
  for i in range(len(lista)):  
    print(f'Nombre: {lista[i]['nombre']}\n'  
          f'Apellido: {lista[i]['apellido']}\n'  
          f'Sector: {lista[i]['sector']}\n'  
          f'Salario: {lista[i]['salario']:.2f}\n')  
  print(f'Fin del listado...')  
  
def salario_promedio(lista):  
  suma_salarios = 0  
  promedio = 0  
  for i in range(len(lista)):  
    suma_salarios += lista[i]['salario']  
  
  promedio = suma_salarios/len(lista)  
  return promedio  
  
opcion = 1  
  
while opcion != 0:  
  nombre, apellido, sector, salario = pedir_datos()  
  empleado = crear_empleado(nombre,apellido,sector,salario)  
  cargar_empleado(lista_empleados,empleado)  
  opcion = int(input(f'Cargar otro empleado ?\n'  
                     f'1. Si\n'  
                     f'0. No\n'  
                     f'Ingrese su opcion: '))  
  
  if opcion == 0:  
    print('Saliendo...')  
    break  
  
mostrar_lista(lista_empleados)  
promedio = salario_promedio(lista_empleados)  
print(f'El promedio es: {promedio:.2f}')
```

---
## 3. Control de stock
Una tienda administra el stock de sus productos.
Cada producto tiene:
- nombre
- stock
El sistema debe permitir:
- [x] registrar productos
- [x] aumentar el stock de un producto existente
- [x] disminuir el stock
- [x] mostrar el inventario

```python
lista_productos = []  
  
def mostrar_menu():  
  opcion = int(input(f'1. Registrar producto\n'  
                     f'2. Aumentar stock\n'  
                     f'3. Disminuir stock\n'  
                     f'4. Mostrar inventario\n'  
                     f'0. Salir\n'  
                     f'Seleccione una opcion: '))  
  
  return opcion  
#---  
def crear_producto(nombre,stock):  
  producto = {}  
  
  producto['nombre'] = nombre  
  producto['stock'] = stock  
  
  return producto  
#---  
def pedir_datos_prod():  
  nombre = input('Ingrese el nombre del producto: ').capitalize()  
  stock = int(input('Ingrese el stock del producto: '))  
  return nombre, stock  
#---  
def cargar_productos(lista,producto):  
  lista.append(producto)  
  print(f'Producto cargado...')  
#---  
def aumentar_stock(lista):  
  for i in range(len(lista)):  
    print(f'{i+1}. {lista[i]["nombre"]}')  
  
  opc_prod = int(input('Seleccione el producto: '))  
  cant_aum = int(input('Ingrese la cantidad de stock a aumentar: '))  
  
  for i in range(len(lista)):  
    if opc_prod == (i + 1):  
      lista[i]['stock'] += cant_aum  
      print(f'Stock actualizado: {lista[i]["stock"]}')  
#---  
def disminuir_stock(lista):  
  for i in range(len(lista)):  
    print(f'{i+1}. {lista[i]["nombre"]}')  
  
  opc_prod = int(input('Seleccione el producto: '))  
  cant_dis = int(input('Ingrese la cantidad de stock a disminuir: '))  
  
  for i in range(len(lista)):  
    if opc_prod == (i + 1):  
      lista[i]['stock'] -= cant_dis  
      print(f'Stock actualizado: {lista[i]["stock"]}')  
#---  
def mostrar_inventario(lista):  
  print('Lista de productos')  
  for i in range(len(lista)):  
    print(f'{i+1}. {lista[i]["nombre"]} - Stock: {lista[i]["stock"]}')  
  print('Fin de inventario')  
  
opcion = 1  
  
while opcion != 0:  
  opcion = mostrar_menu()  
  
  if opcion == 1:  
    nombre,stock = pedir_datos_prod()  
    producto = crear_producto(nombre,stock)  
    cargar_productos(lista_productos,producto)  
  elif opcion == 2:  
    aumentar_stock(lista_productos)  
  elif opcion == 3:  
    disminuir_stock(lista_productos)  
  elif opcion == 4:  
    mostrar_inventario(lista_productos)  
  elif opcion == 0:  
    print('Saliendo del sistema...')  
    break  
  else:  
    print('Opcion no valida')  
  
print(f'Fin del programa')
```

---
## Desafío de razonamiento
Analiza el siguiente código sin ejecutarlo.
```python
contador = 10

def modificar():
    contador = 20
    print(contador)

modificar()

print(contador)
```
Responde:
1. ¿Qué imprime la función `modificar()`?
	Imprime el valor de el contador pero modificado.
2. ¿Qué imprime el último `print()`?
	El ultimo print imprime el valor del contador = 10
3. ¿Por qué ambas salidas son diferentes?
	Porque en la función se crea una variable local a esta, que tiene el mismo nombre que la variable global, pero la global tiene otro valor y esta no se ve modificada dentro de la función.
4. ¿Qué ocurriría si elimináramos la línea `contador = 20` de la función?
	Imprimiría el valor de la variable local
5. ¿En qué situación real considerarías usar una variable global y por qué crees que, en la mayoría de los casos, se recomienda evitarlas?
	Porque a estas variables cualquier función podría modificarlas y esto haría ilegible el programa.