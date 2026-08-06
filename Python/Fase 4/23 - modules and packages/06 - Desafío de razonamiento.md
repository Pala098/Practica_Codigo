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
2. ¿Qué ocurre cuando Python encuentra `import matematica`?
3. ¿Cómo accede `main.py` a la función `multiplicar()`?
4. ¿Qué imprimirá el programa?
5. ¿Qué ventaja aporta separar `matematica.py` de `main.py` en lugar de escribir todo en un único archivo?