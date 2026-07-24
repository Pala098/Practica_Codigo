
## Empresa
**TechStore Analytics**

---
Después del éxito del primer proyecto, ahora la empresa quiere comenzar a tomar decisiones utilizando indicadores de negocio.
Vos formas parte del equipo de datos y te llegan tickets de distintos sectores de la empresa.
Como en un trabajo real, **cada ticket es independiente**.

---
# 🎫 Ticket #1 — Marketing

## 📧 Solicitud

> Necesitamos saber en qué ciudades tenemos más de un cliente para planificar campañas presenciales.
> 
> Queremos ver:
> 
> - la ciudad;
> - la cantidad de clientes.
> 
> Ordená el resultado por la cantidad de clientes de mayor a menor.
---
## Tu tarea
Seguí exactamente la metodología que venimos utilizando.

1. Análisis

```
Análisis

Columnas:
	- ciudad
Tabla(s):
	- Clientes
Condiciones (WHERE):
	- Ninguno
Agrupación (GROUP BY):
	- ciudad
Filtro de grupos (HAVING):
	- having ciudad count(*) > 1
Orden (ORDER BY):
	- order by 
Límite (LIMIT):
	- Ninguno
Operaciones especiales:
	- having
	- count
	- goup by
Observaciones:
	- Se colicita las ciudades donde la cantidad de clientes sea mayor a 1
	- Se solicita un orden por la cantidad de clientes de mayor a menor.
```

---

2. Consulta SQL

---

3. Auto revisión

- ¿Cumple el requerimiento?
- ¿Elegiste las herramientas correctas?
- ¿Existe una forma más simple?
- ¿Hay alguna mejora de legibilidad?
- ¿Qué parte del problema te hizo decidir usar esas herramientas?