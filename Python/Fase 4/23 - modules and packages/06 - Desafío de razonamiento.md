Analizá el siguiente código sin ejecutarlo.

**archivo `matematica.py`**

```
def multiplicar(a, b):
    return a * b
```

**archivo `main.py`**

```
import matematica

resultado = matematica.multiplicar(4, 6)

print(resultado)
```

Respondé:

1. ¿Qué archivo se ejecuta primero al iniciar el programa?
	El archivo que se ejecuta primero es `main.py`.
2. ¿Qué ocurre cuando Python encuentra `import matematica`?
	Permite al archivo `main.py` acceder a las funciones dentro del archivo `matematica.py`
3. ¿Cómo accede `main.py` a la función `multiplicar()`?
	`main.py` accede a la función `multiplicar()` mediante la invocación`matematica.multiplicar()`
4. ¿Qué imprimirá el programa?
	El resultado de ejecutar la función `multiplicar()` con los valores 4 y 6, asignado a la variable resultado. Imprimiendo 12.
5. ¿Qué ventaja aporta separar `matematica.py` de `main.py` en lugar de escribir todo en un único archivo?
	Un codigo mas limpio, donde cada archivo se encarga de algo especifico.