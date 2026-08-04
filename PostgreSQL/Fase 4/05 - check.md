# Actividad de comprensión

## Parte 1 – Conceptos

1. Con tus palabras:
	**¿Qué problema resuelve `CHECK`?**
	No repitas la definición. Explicá qué necesidad cubre.
---
2. Explicá la diferencia entre:
	- `CHECK`
	- `NOT NULL`
	¿En qué se parecen y en qué se diferencian?
---
3. Analizá la siguiente columna:
```
precio NUMERIC NOT NULL CHECK (precio >= 0)
```
Respondé:
1. ¿Qué garantiza `NOT NULL`?
2. ¿Qué garantiza `CHECK`?
3. ¿Se podría guardar un precio de `-100`?
4. ¿Se podría guardar un `NULL`?
5. ¿Se podría guardar `2500`?
Justificá cada respuesta.
---
4. Imaginá que un profesor quiere almacenar notas de exámenes.
	¿Qué condición escribirías conceptualmente (sin preocuparte por la sintaxis exacta) para impedir que existan notas menores que 0 o mayores que 10?
	Explicá el razonamiento.

---
# Parte 2 – Diseño de TechStore
Indicá si usarías `CHECK` y qué regla aplicarías.

| Columna            | ¿CHECK?   | Regla | Justificación |
| ------------------ | --------- | ----- | ------------- |
| `precio`           | ¿Sí o No? | ?     | ?             |
| `stock`            | ¿Sí o No? | ?     | ?             |
| `descuento`        | ¿Sí o No? | ?     | ?             |
| `nombre`           | ¿Sí o No? | ?     | ?             |
| `cantidad_vendida` | ¿Sí o No? | ?     | ?             |

---
# 🧩 Desafío de análisis

El dueño de TechStore propone:

> "No hace falta poner `CHECK`. Los empleados saben que un precio no puede ser negativo."

Como diseñador de la base de datos, respondé:
- ¿Estás de acuerdo o no?
- ¿Qué ventaja aparente tiene esa idea?
- ¿Qué riesgos genera confiar únicamente en que los usuarios nunca se equivocarán?