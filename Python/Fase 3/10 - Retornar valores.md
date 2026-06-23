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
>- [ ] Completado

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

## 4. Registro de empleados
Crear una función que reciba:
- nombre
- apellido
- sector
y genere la estructura de datos correspondiente para representar un empleado.
Registrar varios empleados utilizando esa función.
Finalmente mostrar el listado completo.
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
2. ¿Qué valor queda almacenado en `resultado`?
3. ¿Qué imprime el programa?
4. ¿Qué ocurriría si reemplazáramos `return a + b` por `print(a + b)`?
5. ¿Cuál es la diferencia conceptual entre mostrar un dato y devolver un dato?