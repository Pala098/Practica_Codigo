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
## 2. Registro de cursos
Crear un set vacío, solicitar 5 nombres de cursos.
Agregar cada curso utilizando -> `add()`
Al finalizar mostrar todos los cursos registrados.
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
2. ¿Por qué no aparecen algunos repetidos?
3. ¿Cuál es la característica de los sets que provoca este comportamiento?