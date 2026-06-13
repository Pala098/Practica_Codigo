## 1. Invitados únicos
Crear el siguiente set: 
```
invitados = {
    "Juan",
    "Pedro",
    "Juan",
    "María",
    "Pedro"
}
```
Mostrar: 
- el set completo
- cantidad de invitados únicos

```python
invitados = {
	'Juan',
	'Pedro',
	'Juan',
	'Maria',
	'Pedro'
}

for x in invitados:
	print(x)

print(f'Cantidad de invitados unicos: {len(invitados)}')
```

## 2. Registro de cursos
Crear un set vacío, solicitar 5 nombres de cursos.
Agregar cada curso utilizando -> `add()`
Al finalizar mostrar todos los cursos registrados.

```python
nombres_curso = set()
contador = 0

while contador <= 5:
	nombre = input(f'Ingrese el nombre del curso: ').capitalize()
	nombres_curso.add(nombre)
	contador += 1
	print(f'Dato cargado...\n')

for curso in nombres_curso:
	print(f'- {curso}')
```

## 3. Búsqueda de usuario
Crear un set:
```
usuarios = {
    "admin",
    "paulo",
    "maria",
    "juan"
}
```
Solicitar un usuario.
Indicar:
- usuario encontrado
- usuario no encontrado

```python
usuarios = {
	'Admin',
	'Diana',
	'Maria',
	'Juan'
}

usuario = input('Ingrese su usuario: ').capitalize()

print(f'El usuario existe? --> {usuario in usuarios}')
```

## 4. Cliente únicos
Crear una lista:
```
clientes = [
    "Juan",
    "Pedro",
    "Juan",
    "María",
    "Pedro",
    "Lucas"
]
```
Convertirla en set y mostrar:
- clientes únicos
- cantidad de clientes únicos

```python
clientes = [
	'Juan',
	'Pedro',
	'Juan',
	'Maria',
	'Pedro',
	'Lucas'
]

lista_clientes = set(clientes)

print(f'Lista clientes unicos: {lista_clientes}\n')
print(f'Cantidad de clientes unicos: {len(lista_clientes)}')

```

## 5. Integrador
Una empresa registra empleados que asistieron a dos capacitaciones:
```
capacitacion_python = {
    "Juan",
    "María",
    "Pedro",
    "Ana"
}

capacitacion_sql = {
    "María",
    "Pedro",
    "Lucas",
    "Ana"
}
```
Mostrar:
1. Empleados que asistieron a ambas capacitaciones
2. Todos los empleados que asistieron al menos a una capacitación
3. Empleados que asistieron a python pero no a sql

```python
capacitacion_python = {
	'Juan',
	'Maria',
	'Pedro',
	'Ana'
}

capacitacion_sql = {
	'Maria',
	'Pedro',
	'Lucas',
	'Ana'
}

resultado = capacitacion_python | capacitacion_sql
print(f'Empleados que asistieron a ambas capacitaciones: {resultado}\n')
resultado = capacitacion_python & capacitacion_sql
print(f'Empleados que asistieron a almenos una capacitacion: {resultado}\n')
resultado = capacitacion_python - capacitacion_sql
print(f'Empleados que asistieron solo a Python: {resultado}\n')


```

## Razonamiento
Sin ejecutar:
```python
numeros = {10, 20, 20, 30}

numeros.add(30)
numeros.add(40)

print(numeros)
```
Preguntas:
1. ¿Qué valores contendrá el set?

> Los valores que contendrá son -> {10,20,30,40}

2. ¿Por qué no aparecen algunos repetidos?

> Porque al imprimir un set este no muestra, o no almacena, datos repetidos.

3. ¿Cuál es la característica de los sets que provoca este comportamiento?

> 