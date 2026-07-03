## Consulta A
```sql
select nombre from clientes where nombre like 'A%';
```
**Preguntas:**
1. ¿Qué nombres aparecerán?
	Solo se mostrara un valor: Ana
2. ¿Por qué?
	Porque es el único valor que cumple con el criterio de la consulta, que es que inicie con 'A', después de este no importa que caracteres haya.
---
## Consulta B
```sql
select ciudad from clientes where ciudad like '%a';
```
**Preguntas:**
1. ¿Qué ciudades aparecerán?
	Las ciudades que aparecerán son: La Plata, Córdoba, Mendoza y La Plata.
2. ¿Por qué Rosario no aparecería?
	Porque Rosario contiene 'a', pero ni inicia ni termina con este carácter.
---
## Consulta C
```sql
select producto from productos where producto like '%te%';
```
**Preguntas:**
1. ¿Qué productos aparecerán?
	Aparecerá notebook.
2. ¿Qué significa el `%` que está antes y después de `"te"`?
	Significa que no importa que caracteres tenga antes o después.