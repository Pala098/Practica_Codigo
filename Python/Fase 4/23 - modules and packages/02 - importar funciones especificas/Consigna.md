Crear:

```
productos.py
```

Funciones:

- `calcular_iva(precio)`
- `calcular_descuento(precio)`

En `main.py` importar únicamente esas funciones utilizando:

```
from productos import calcular_iva, calcular_descuento
```

Solicitar un precio al usuario y mostrar:

- IVA
- descuento
- precio final

### `main.py`
```python
from productos import calcular_iva, calcular_descuento

precio = float(input(f'Ingrese el precio del producto: \n'
                     f'> '))

precio_final = precio + calcular_iva(precio) + calcular_descuento(precio)

print(f'Precio: ${precio:.2f}\n'
      f'IVA: ${calcular_iva(precio):.2f}\n'
      f'Descuento 15%: ${calcular_descuento(precio):.2f}\n'
      f'PRECIO FINAL: ${precio_final:.2f}\n')

```

### `productos.py`
```python
def calcular_iva(precio):
  iva = precio * 0.21
  return iva

def calcular_descuento(precio):
  descuento = precio * 0.15
  return descuento

```

> [!bug] Corrección
> Tenés:
> ```
> calcular_iva(precio)
> calcular_descuento(precio)
> ```
> pero luego volvés a llamarlas otra vez para imprimir.
> Normalmente se hace:
> ```python
> iva = calcular_iva(precio)
> descuento = calcular_descuento(precio)
> total = ...
> print(iva)
> print(descuento)
> ```
> Se calcula una vez, no varias.