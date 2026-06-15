## 1. Perfil de usuario
Crear un diccionario: 
```
usuario = {
    "nombre": "valor",
    "edad": valor,
    "ciudad": "valor"
}
```
Mostrar cada valor utilizando su clave.

```python
usuario = {
	'nombre' : 'Juan',
	'edad' : 28,
	'ciudad' : 'Rio Negro'
}

for clave in usuario:
	print(usuario[clave])
```

## 2. Registro de producto
Crear un diccionario vacío.
Solicitar:
- nombre
- precio
- stock
Guardar los datos utilizando claves descriptivas.
Luego mostrar:
```
Producto: Mouse
Precio: $15000
Stock: 25
```

```python
producto = {}

producto['nombre'] = input('Nombre del producto: ').capitalize()
producto['precio'] = float(input('Precio del producto: $'))
producto['stock'] = int(input('Stock del producto: '))

for clave in producto:
	print(f'{clave} : {producto[clave]}')

```

## 3. Actualización de edad
Crear:
```
persona = {
    "nombre": "Juan",
    "edad": 25
}
```
Solicitar una nueva edad, actualizar el diccionario y mostrarlo nuevamente.

```python
persona = {
	'nombre' : 'Juan',
	'edad' : 25
}
print('Datos actuales')
for clave in persona:
	print(f'{clave} : {persona[clave]}')

persona['edad'] = int(input('Ingrese la nueva edad: '))

print('Datos actualizados')
for clave in persona:
	print(f'{clave} : {persona[clave]}')
```

## 4. Inventario
Crear un diccionario:
```
producto = {
    "nombre": "Teclado",
    "precio": 25000,
    "stock": 10
}
```
Recorrerlo utilizando --> `items()`
Mostrar:
```
nombre : Teclado
precio : 25000
stock : 10
```

```python
producto = {
	'nombre' : 'Teclado',
	'precio' : 25000,
	'stock' : 10
}

for clave,valor in producto.items():
	print(clave, valor)

```

## 5. Integrador
Registrar información de 3 empleados.
Para cada empleado solicitar:
- nombre
- edad
- sector
Guardar cada empleado en un diccionario.
Luego guardar todos los diccionarios dentro de una lista y mostrar todos los empleados registrados.

```python
empleados = []

for i in range(0,3):
  empleado = {}

  nombre = input('Ingrese su nombre: ').capitalize()
  edad = int(input('Ingrese su edad: '))
  sector = input('Ingrese su sector: ').capitalize()

  empleado['nombre'] = nombre
  empleado['edad'] = edad
  empleado['sector'] = sector

  empleados.append(empleado)

  print(f'\nDatos cargados correctamente !/n')

print(f'Cantidad de empleados registrados: {len(empleados)}')

print(empleados)
```

## Razonamiento
Sin ejecutar:
```python
producto = {
    "nombre": "Mouse",
    "precio": 15000
}

producto["stock"] = 20
producto["precio"] = 18000

print(producto)
```
Preguntas:
1. ¿Qué contiene el diccionario al final?

	> Contiene:
	> {
	> 'nombre' : 'Mouse',
	> 'precio' : 18000,
	> 'stock' : 20
	> }

2. ¿Qué línea agrega una nueva clave?

	>producto['stock'] = 20

3. ¿Qué línea modifica un valor existente?

	>producto['precio'] = 18000

4. ¿Por qué no se utiliza un índice como en las listas?

	>Porque los diccionarios almacenan los datos mediante una relación que es clave -> valor, esto para evitar depender de recordar la posición o índice.