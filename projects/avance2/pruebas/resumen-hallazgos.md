# Resumen de Hallazgos — Inventario del Valle

**Ejecutado por:** Angel Segura Méndez  
**Fecha:** 2026-04-03  
**Rama evaluada:** `Migracion_SQLITE`  
**Commit evaluado:** `f7bde67`

---

## HAL-001 — Producto inactivo sigue visible en módulo de Ventas

| Campo | Detalle |
|-------|---------|
| **ID** | HAL-001 |
| **Severidad** | Alta |
| **Módulo** | Productos → Ventas |
| **Tipo** | Bug funcional |
| **Caso relacionado** | CP-M006 |
| **Estado** | Confirmado |

**Descripción:**  
Al marcar un producto como inactivo en el módulo de Productos, dicho producto continúa apareciendo disponible para seleccionar al crear una nueva venta.

**Impacto:**  
Se pueden registrar ventas de productos que fueron dados de baja intencionalmente, generando inconsistencias en el inventario y los reportes.

**Recomendación:**  
Agregar filtro `WHERE PRO_Estado = 'A'` (activo) en la consulta que carga productos disponibles para venta.

---

## HAL-002 — Buscador de productos no filtra por código

| Campo | Detalle |
|-------|---------|
| **ID** | HAL-002 |
| **Severidad** | Media |
| **Módulo** | Productos |
| **Tipo** | Funcionalidad incompleta |
| **Caso relacionado** | CP-A003 |
| **Estado** | Confirmado |

**Descripción:**  
El buscador del módulo de Productos solo filtra por nombre. Al ingresar un código de producto (ej: "ARE-001"), no retorna ningún resultado aunque el producto exista con ese código.

**Impacto:**  
Los usuarios que conozcan el código del producto pero no el nombre exacto no pueden encontrarlo mediante el buscador, reduciendo la eficiencia operativa.

**Recomendación:**  
Incluir el campo `PRO_Codigo` en el filtro de búsqueda, de forma que busque por nombre O código.

---

## HAL-003 — No existe historial de movimientos de inventario

| Campo | Detalle |
|-------|---------|
| **ID** | HAL-003 |
| **Severidad** | Alta |
| **Módulo** | Inventario |
| **Tipo** | Funcionalidad faltante |
| **Caso relacionado** | CP-A004 |
| **Estado** | Confirmado |

**Descripción:**  
El módulo de Inventario permite registrar entradas y salidas de mercadería, pero no existe ninguna opción para consultar el historial de movimientos registrados (auditoría de entradas, salidas y ajustes).

**Impacto:**  
No es posible hacer trazabilidad de los movimientos de inventario. No se puede verificar quién realizó qué movimiento ni cuándo, lo cual es crítico para auditorías y control de inventario.

**Recomendación:**  
Agregar una sección o pestaña de "Historial de movimientos" en el módulo de Inventario que liste los movimientos con fecha, tipo, cantidad, producto y usuario responsable.

---

## HAL-004 — No hay indicador visual de stock bajo en módulo Inventario

| Campo | Detalle |
|-------|---------|
| **ID** | HAL-004 |
| **Severidad** | Media |
| **Módulo** | Inventario |
| **Tipo** | Mejora de usabilidad |
| **Caso relacionado** | CP-A009 |
| **Estado** | Confirmado |

**Descripción:**  
El módulo de Inventario muestra el stock de todos los productos, pero no diferencia visualmente los productos con stock bajo o agotado. El Dashboard sí muestra el contador de "Stock Bajo", pero al entrar al módulo de Inventario no hay colores, íconos ni etiquetas que identifiquen productos críticos.

**Impacto:**  
El usuario debe revisar manualmente cada producto para identificar cuáles necesitan reabastecimiento, lo que aumenta el riesgo de quedarse sin stock de productos importantes.

**Recomendación:**  
Agregar indicadores visuales (color rojo/amarillo, ícono de alerta) para productos con stock igual a 0 o por debajo de un umbral definido.

---

## HAL-005 — Campo teléfono en Emprendedoras acepta letras

| Campo | Detalle |
|-------|---------|
| **ID** | HAL-005 |
| **Severidad** | Baja |
| **Módulo** | Emprendedoras |
| **Tipo** | Validación faltante |
| **Caso relacionado** | CP-A008 |
| **Estado** | Confirmado |

**Descripción:**  
El campo de teléfono en el formulario de Emprendedoras acepta cualquier caracter, incluyendo letras. No existe validación de formato numérico.

**Impacto:**  
Se pueden guardar números de teléfono inválidos (ej: "abc123"), lo que genera datos de contacto incorrectos e inutilizables.

**Recomendación:**  
Agregar validación en el campo teléfono para aceptar solo dígitos numéricos, con un formato esperado de 8 dígitos (estándar Costa Rica).

---

## HAL-006 — US-14 (Gestión por local) no está implementada

| Campo | Detalle |
|-------|---------|
| **ID** | HAL-006 |
| **Severidad** | Media |
| **Módulo** | — |
| **Tipo** | Funcionalidad no implementada |
| **Caso relacionado** | CP-A014 |
| **Estado** | Confirmado |

**Descripción:**  
La User Story US-14 requiere gestionar información de diferentes locales o puntos de venta. No existe ningún módulo, sección ni campo relacionado con locales en la interfaz de la aplicación.

**Impacto:**  
Si la asociación necesita expandirse a múltiples locales, el sistema no tiene soporte para esto.

**Recomendación:**  
Implementar el módulo de gestión de locales según los requerimientos de la US-14.

---

## HAL-007 — Botón "Destacar producto" no funciona

| Campo | Detalle |
|-------|---------|
| **ID** | HAL-007 |
| **Severidad** | Alta |
| **Módulo** | Productos |
| **Tipo** | Bug funcional |
| **Caso relacionado** | CP-A016 |
| **Estado** | Confirmado |

**Descripción:**  
En el módulo de Productos existe un botón para marcar un producto como "destacado" (para mostrarlo en la página web). Al presionar el botón, no ocurre ninguna acción visible: no cambia de estado, no muestra confirmación ni error.

**Impacto:**  
La User Story US-16 (destacar productos en la página principal) no puede cumplirse. Los administradores no pueden promover productos en el sitio web desde la aplicación.

**Recomendación:**  
Revisar el handler del botón de destacado en el componente de productos y verificar que el IPC correspondiente esté registrado y funcionando correctamente.

---

## Tabla resumen de hallazgos

| ID | Severidad | Módulo | Tipo | Estado |
|----|-----------|--------|------|--------|
| HAL-001 | Alta | Productos → Ventas | Bug funcional | Confirmado |
| HAL-002 | Media | Productos | Funcionalidad incompleta | Confirmado |
| HAL-003 | Alta | Inventario | Funcionalidad faltante | Confirmado |
| HAL-004 | Media | Inventario | Usabilidad | Confirmado |
| HAL-005 | Baja | Emprendedoras | Validación faltante | Confirmado |
| HAL-006 | Media | — | No implementado | Confirmado |
| HAL-007 | Alta | Productos | Bug funcional | Confirmado |
