## 1. Credencial de acceso
Crear una función que reciba los datos de una persona y muestre una credencial similar a: 
```
--------------------
USUARIO REGISTRADO
--------------------
Nombre: Juan Pérez
Sector: Ventas
```
Luego utilizarla para mostrar la información de al menos 3 personas diferentes.

```python
def mostrar_credencial(personas, aux):
	print(f'{aux}\nUSUARIOS REGISTRADOS\n{aux}')
	for persona in personas:
		print(f'Nombre: {persona['nombre']}\nSector: {persona['sector']}\n{aux}')

deco = '-' * 20

personas_list = []

for i in range(3):
	persona = {}
	
	nombre = input('Ingrese su nombre: ').capitalize()
	sector = input('Ingrese su sector de trabajo: ').capitalize()
	
	persona['nombre'] = nombre
	persona['sector'] = sector
	
	personas_list.append(persona)

mostrar_credencial(personas_list,deco)
```

## 2. Resumen de compra
Una tienda registra compras durante el día.
Crear una función que reciba:
- nombre del cliente
- cantidad de productos
- importe total
y muestre un resumen de la operación.
Probar la función con varios clientes.

```python
def mostrar_menu(aux):  # --> funcion que muestra el menu
    print(f'..:: MENU ::..\n{aux}\n1. Cargar un producto\n0. Salir y mostrar resumen')


def calculo_imp_total(cantidad, valor):
    total = cantidad * valor
    producto['total'] = total


def mostrar_resumen(lista, aux):
    print(f'..:: RESUMEN DE COMPRA ::..\n{aux}')
    for dato in lista:
        print(
            f'- Nombre cliente: {dato['nombre']}\n- Cantidad productos: {dato['cantidad']}\n- Importe total: {dato['total']}\n{aux}')


deco = '-' * 20
ventas_list = []  # --> lista vacia para guardar los datos

opcion = 1  # --> opcion para cortar con el ciclo o cargar un nuevo producto

while opcion != 0:
    mostrar_menu(deco)
    print(deco)
    opcion = int(input('Seleccione un opcion: '))

    if opcion == 1:
        producto = {}

        nombre_cli = input('Ingrese nombre: ')
        cant_prod = int(input('Ingrese la cantidad de productos: '))
        impor_uni = float(input('Ingrese el importe individual: '))

        producto['nombre'] = nombre_cli
        producto['cantidad'] = cant_prod
        calculo_imp_total(cant_prod, impor_uni)

        ventas_list.append(producto)
        print(f'{deco}\nVenta cargada correctamente...\n{deco}')
    elif opcion == 0:
        mostrar_resumen(ventas_list, deco)
        print(f'\nSaliendo del programa...')
        break
    else:
        print('Opcion erronea.\nSaliendo del programa...')
        break
```
## 3. Catálogo
Crear una lista con varios productos.
Construir una función que reciba dicha lista y muestre el catálogo numerado.
La función debe poder reutilizarse con cualquier lista de productos.

```python
def mostrar_menu(aux):
    print(f'..:: MENU ::..\n{aux}\n1. Cargar un producto\n0. Salir y mostrar catalogo\n{aux}')


def cargar_producto(lista, aux):
    print(f'Cargar Producto\n{aux}')
    nombre_producto = input('Ingrese el producto: ')
    lista.append(nombre_producto)
    print(f'{aux}\nProducto agregado...\n{aux}')


def mostrar_catalogo(lista, aux):
    print(f'Mostrar Catalogo\n{aux}')
    for i in range(len(lista)):
        print(f'{i + 1}. {lista[i]}')
    print(f'{aux}\nFin del caltalogo...\n{aux}')


lista_productos = []

# variables
opcion = 1
deco = '-' * 20

while opcion == 1:
    mostrar_menu(deco)
    opcion = int(input('Seleccione una opcion: '))

    if opcion == 1:
        cargar_producto(lista_productos, deco)
    elif opcion == 0:
        mostrar_catalogo(lista_productos, deco)
        print(f'Saliendo del programa...\n{deco}')
        break
    else:
        print('Error: opcion incorrecta...')

```

## 4. Ficha de empleado
Registrar 3 empleados utilizando diccionarios.
Crear una función que reciba un empleado y muestre toda su información de forma ordenada.
Luego recorrer la colección de empleados utilizando esa función.

```python
def cargar_empleado(lista, aux, cant):
    print(f'..:: Cargar empleado ::..\n{aux}\nDatos empleado: {cant + 1}\nMaximo de empleados permitido: 3\n{aux}')
    empleado = {}

    if cant <= 2:
        nombre = input('Ingrese su nombre: ')
        apellido = input('Ingrese su apellido: ')
        sector = input('Ingrese su sector: ')

        empleado['nombre'] = nombre
        empleado['apellido'] = apellido
        empleado['sector'] = sector

        lista.append(empleado)
        print(f'{aux}\nEmpleado cargado...\n{aux}')

def mostrar_menu(aux):
    print(
        f'..:: MENU ::..\n{aux}\n1. Cargar empleado\n2. Mostrar informacion de un empleado\n3. Mostrar listado de empleados\n0. Salir\n{aux}')


def mostrar_nombre_empleados(lista, aux):
    print(f'..:: Dato de empleado ::..\n{aux}')
    print(f'Listado de empleados\n{aux}')
    for i in range(len(lista)):
        print(f'{i + 1}. {lista[i]['nombre']}')
    print(aux)
    opcion = int(input('Ingrese el indice del empleado: '))
    print(aux)
    for i in range(len(lista)):
        if i == opcion - 1:
            print(f'- Nombre: {lista[i]['nombre']}\n- Apellido: {lista[i]['apellido']}\n- Sector: {lista[i]['sector']}\n{aux}')

def mostrar_listado_empleados(lista,aux):
    print(f'..:: Listado de empleados ::..\n {aux}')
    for i in range(len(lista)):
        print(f'Empleado: {i + 1}\n{aux}\n'
              f'Nombre completo: {lista[i]['nombre']} {lista[i]['apellido']}\n'
              f'Sector: {lista[i]['sector']}\n{aux}')
    print('Fin del listado...')

lista_empleados = []
# constante
LIMITE = 3

# variables
deco = '-' * 25
opcion = 1
contador = 0

while opcion != 0:
    mostrar_menu(deco)
    opcion = int(input('Seleccione una opcion: '))
    print(deco)

    if opcion == 1 and contador < LIMITE:
        cargar_empleado(lista_empleados, deco, contador)
        contador += 1
    elif opcion == 2:
        mostrar_nombre_empleados(lista_empleados,deco)
    elif opcion == 3:
        mostrar_listado_empleados(lista_empleados,deco)
    elif opcion == 4: 
        print(f'Saliendo del sistema...')
        break
    else:
        print('ERROR: Opcion ingresada incorrecta...')		
```

## 5. Control de capacitación
Una empresa registró los asistentes a un curso.
Crear una función que reciba una colección de participantes y muestre:
- cantidad total de participantes
- listado completo
Probarla con al menos dos grupos distintos,

```python
def mostrar_menu(aux):
    print(
        f'..:: MENU ::..\n{aux}\n1. Cargar nuevo cursante\n2. Mostrar cantidad de participantes\n3. Mostrar listado completo\n0. Salir\n{aux}')


def cargar_participante(curso1, curso2, aux):
    print(f'CARGAR PARTICIPANTE\n{aux}')
    participante = {}

    nombre = input('Ingrese su nombre: ')
    curso = int(input('A que curso pertenece (1 o 2): '))

    participante['nombre'] = nombre
    participante['curso'] = curso

    if participante['curso'] == 1:
        curso1.append(participante)
        print(f'{aux}\nParticipante cargado...\n{aux}')
    elif participante['curso'] == 2:
        curso2.append(participante)
        print(f'{aux}\nParticipante cargado...\n{aux}')
    else:
        print(f'{aux}\nCurso inexisntente\n{aux}')


def mostrar_cantidad(curso1, curso2, aux):
    print(f'CANTIDAD DE PARTICIPANTES\n{aux}')
    cant_c1 = len(curso1)
    cant_c2 = len(curso2)
    print(f'- Curso 1: {cant_c1}\n- Curso 2: {cant_c2}\n{aux}')


def mostrar_list_completo(curso1, curso2, aux):
    print(f'MOSTRAR LISTADO COMPLETO\n{aux}')
    print(f'1. Ver listado curso 1\n2. Ver listado curso 2\n{aux}')
    sel_curso = int(input('Seleccione el curso: '))

    if sel_curso == 1:
        print(f'{aux}\nLISTADO CURSO 1\n{aux}\nCantidad total: {len(curso1)}\n{aux}')
        for i in range(len(curso1)):
            print(f'- Nombre: {curso1[i]['nombre']}')
        print(f'{aux}\nListado finalizado...\n{aux}')
    elif sel_curso == 2:
        print(f'{aux}\nLISTADO CURSO 2\n{aux}\nCantidad total: {len(curso2)}\n{aux}')
        for i in range(len(curso2)):
            print(f'- Nombre: {curso2[i]['nombre']}')
        print(f'{aux}\nListado finalizado...\n{aux}')
    else:
        print(f'{aux}\nERROR: opcion ingresada inexistente\n{aux}')


list_curso_1 = []
list_curso_2 = []

# variables
deco = '-' * 25
opcion = 1

while opcion != 0:
    mostrar_menu(deco)
    opcion = int(input('Seleccione una opcion: '))
    print(deco)

    if opcion == 1:
        cargar_participante(list_curso_1, list_curso_2, deco)
    elif opcion == 2:
        mostrar_cantidad(list_curso_1, list_curso_2, deco)
    elif opcion == 3:
        mostrar_list_completo(list_curso_1, list_curso_2, deco)
    elif opcion == 0:
        print(f'Saliendo del sistema...\n{deco}')
        break
    else:
        print(f'ERROR: opcion ingresada erronea...')
```

## Desafío razonamiento
Sin ejecutar: 
```python
def mostrar(nombre):
    print(f'Hola {nombre}')

usuario = 'Paulo'

mostrar(usuario)
```
Responder:
1. ¿Qué valor recibe el parámetro `nombre`?
	Recibe el argumento de la variable 'nombre'
2. ¿Qué imprime el programa?
	El programa imprime 'Hola Paulo'
3. ¿Cuál es el argumento?
	El argumento es el valor de la variable usuario 
4. ¿Cuál es el parámetro?
	El parametro es nombre.
5. ¿Qué ocurriría si se ejecutara solamente?
```python
mostrar()
```
Dara error, porque la funcion necesita de un parametro.