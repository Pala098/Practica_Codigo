## 3. Registro de empleados
Una empresa necesita registrar exactamente 3 empleados.
Guardar:
- `nombres = []`
- `edades = []`
Solicitar nombre y edad para cada uno.
Al finalizar mostrar:
```
Empleado 1: Juan - 25 años
Empleado 2: María - 31 años
Empleado 3: Pedro - 28 años
```
Y además indicar el empleado con mas caracteres en se nombre.

```python
nombres = []
edades = []
mas_caracteres = ''

for i in range(0,3): # --> carga de datos
	nombre = input('Ingrese su nombre: ').capitalize()
	edad = int(input('Ingrese su edad: '))
	
	nombres.append(nombre)
	edades.append(edad)
	
print(f'\nDatos cargados...\n')
	
for x in range(len(nombres)): # --> muestra de datos
	pring(f'Empleado {x + 1}: {nombres[x]} - {edades[x]} años')
	
	if len(nombres[x]) > len(mas_caracteres):
		mas_caracteres = nombres[x]

print(f'\nEmpleado con mas caracteres en su nombre: {mas_caracteres}')

```