Crear:

```
empleados.py
```

Funciones:

- `salario_anual()`
- `salario_mensual()`

Importarlo usando:

```
import empleados as emp
```

Utilizar ambas funciones desde `main.py`.

### `main.py`
```python
import empleados as emp

pago_por_dia = float(input(f'Ingrese el pago diario que recibe: \n> $'))

print(f'Pago diario: ${pago_por_dia:.2f}\n'
      f'Salario anual aprox.: ${emp.salario_anual(pago_por_dia):.2f}\n'
      f'Salario mensual aprox.: ${emp.salario_mensual(pago_por_dia):.2f}')

```

### `empleados.py`
```python
def salario_anual(salario):
  return salario * 276

def salario_mensual(pago):
  return pago * 23
```
