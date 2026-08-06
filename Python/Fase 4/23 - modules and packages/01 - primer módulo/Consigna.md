Crear un archivo:

```
calculadora.py
```

Con las funciones:

- `sumar()`
- `restar()`

Luego crear:

```
main.py
```

Importar el módulo completo usando:

```
import calculadora
```

y utilizar ambas funciones.

### `main.py`
```python
import calculadora

num_1 = int(input(f'Ingrese el primer numero:\n'
                  f'> '))
num_2 = int(input(f'Ingrese el segundo numero:\n'
                  f'> '))

print(f'SUMA\n'
      f'{calculadora.sumar(num_1,num_2)}')

print(f'RESTA\n'
      f'{calculadora.restar(num_1,num_2)}')

```

### `calculadora.py`
```python
def sumar(a,b):
  return a+b

def restar(a,b):
  return a-b

```