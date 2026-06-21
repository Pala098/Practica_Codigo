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
def mostrar_menu(aux): # --> funcion que muestra el menu
	print(f'..:: MENU ::..\n{aux}\n1. Cargar un producto\n0. Salir y mostrar resumen\n')

def calculo_imp_total(cantidad, valor):
	total = cantidad * valor
	producto['total'] = total
	
def mostrar_resumen(lista,aux):
	print(f'..:: RESUMEN DE COMPRA ::..\n{aux}')
	for dato in lista:
		print(f'- Nombre cliente: {dato['nombre']}\nCantidad productos: {dato['cantidad']}\n Importe total: {dato['total']}\n{aux}')
		

deco = '-' * 20
ventas_list = [] # --> lista vacia para guardar los datos

opcion = 1 # --> opcion para cortar con el ciclo o cargar un nuevo producto

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
		mostra_resumen(ventas_list,deco)
		print(f'\nSaliendo del programa...')
		break
	else:
		print('Opcion erronea.\nSaliendo del programa...')
		break
	
```


```python
def calculo_total(cant_prod, precio_ind):
	total = cant_prod * precio_ind

def mostrar_menu():
	print(f'..::Menu::..\n{deco}\n 1. Cargar cliente\n 0. Salir y mostrar resumen')

def mostrar_resumen(registro,aux):
	print(f'..:: RESUMEN FINAL ::..\n{aux}')
	for nombre, cantidad, total in registro.items():
		print(f'- Nombre: {nombre}\n- Cantidad de productos: {cantidad}\nImporte total: ${total.:2f}')

# variables
opcion = 1
deco = '-' * 20
numero_dia = 1

registro_ventas = {}

while True: ## manejo por dias
	print(f'Carga ventas día {numero_dia}')
	ventas_del_dia = []
	
	while True: # --> manejo ventas de un dia
		mostrar_menu()
		opcion = int(input('Seleccione una opción: '))
		if opcion == 1:
			venta = {}
			
			nombre = input('Ingrese nombre del cliente: ')
			cant_prod = int(input('Ingrese la cantidad de productos: '))
			precio_unit = float(input('Ingrese el precio individual: '))
			impor_total = calculo_total(cant_prod,precio_unit)
			
			venta['nombre'] = nombre
			venta['cantidad'] = cant_prod
			venta['total'] = impor_total
			
			ventas_del_dia.append(venta)
			print(f'{deco}\nDatos cargados...\n{deco}')
		elif opcion == 0: 
			break
		else:
			print(f'ERROR: opcion erronea.\nSaliendo del sistema...')
			break
		
	registro_ventas[f'Dia {numero_dia}'] = ventas_del_dia
	
	numero_dia += 1

mostrar_resumen(registro_ventas,deco)
```

## 3. Catálogo
Crear una lista con varios productos.
Construir una función que reciba dicha lista y muestre el catálogo numerado.
La función debe poder reutilizarse con cualquier lista de productos.
## 4. Ficha de empleado
Registrar 3 empleados utilizando diccionarios.
Crear una función que reciba un empleado y muestre toda su información de forma ordenada.
Luego recorrer la colección de empleados utilizando esa función.
## 5. Control de capacitación
Una empresa registró los asistentes a un curso.
Crear una función que reciba una colección de participantes y muestre:
- cantidad total de participantes
- listado completo
Probarla con al menos dos grupos distintos.
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
2. ¿Qué imprime el programa?
3. ¿Cuál es el argumento?
4. ¿Cuál es el parámetro?
5. ¿Qué ocurriría si se ejecutara solamente?
```python
mostrar()
```