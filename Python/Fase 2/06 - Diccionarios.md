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
## 3. Actualización de edad
Crear:
```
persona = {
    "nombre": "Juan",
    "edad": 25
}
```
Solicitar una nueva edad, actualizar el diccionario y mostrarlo nuevamente.
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
## 5. Integrador
Registrar informacion de 3 empleados.
Para cada empleado solicitar:
- nombre
- edad
- sector
Guardar cada empleado en un diccionario.
Luego guardar todos los diccionarios dentro de una lista y mostrar todos los empleados registrados.
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
2. ¿Qué línea agrega una nueva clave?
3. ¿Qué línea modifica un valor existente?
4. ¿Por qué no se utiliza un índice como en las listas?