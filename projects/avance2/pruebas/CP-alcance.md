# Pruebas de Alcance (User Stories) — Inventario del Valle

**Ejecutado por:** Angel Segura Méndez  
**Fecha:** 2026-04-03  
**Tipo:** Pruebas de Alcance  
**Rama evaluada:** `Migracion_SQLITE`  
**Usuario de prueba:** test@inventario.local / test123

---

### CP-A001: US-1 — Gestión de productos (CRUD completo)

| Campo | Valor |
|-------|-------|
| **ID** | CP-A001 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Productos |
| **Nombre** | US-1: Registrar, editar y eliminar productos |
| **Tipo de prueba** | Alcance |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. Usuario autenticado con permiso Administración.

**Datos de prueba:**
- Producto: nombre `Producto Eliminar`, código `PRD-DEL-01`, precio ₡100

**Pasos:**
1. Crear el producto con los datos indicados.
2. Editar el precio del producto.
3. Eliminar el producto (sin ventas asociadas).

**Resultado esperado:** CRUD completo funciona: crear, editar y eliminar.

**Resultado obtenido:** El producto se creó, editó y eliminó correctamente. El sistema también previene eliminar productos con ventas asociadas (verificado en CP-I005).

---

### CP-A002: US-2 — Gestión de categorías (CRUD completo)

| Campo | Valor |
|-------|-------|
| **ID** | CP-A002 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Categorías |
| **Nombre** | US-2: Crear, editar y eliminar categorías |
| **Tipo de prueba** | Alcance |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. Usuario autenticado con permiso Administración.

**Datos de prueba:**
- Categoría: nombre `Prueba`, código `PRB-001`

**Pasos:**
1. Crear categoría "Prueba".
2. Eliminar la categoría.

**Resultado esperado:** CRUD de categorías funciona correctamente.

**Resultado obtenido:** La categoría se creó y eliminó correctamente. También se verificó que al ingresar un código existente, el sistema actualiza en lugar de duplicar.

---

### CP-A003: US-3 — Búsqueda de productos

| Campo | Valor |
|-------|-------|
| **ID** | CP-A003 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Productos |
| **Nombre** | US-3: Buscar productos por nombre y otros filtros |
| **Tipo de prueba** | Alcance |
| **Estado** | Parcial |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. Existen productos en el sistema.

**Datos de prueba:**
- Búsqueda por nombre: "pulsera" → encuentra "Pulsera Artesanal"
- Búsqueda por código: "ARE-001" → no encuentra "Aretes de plata"
- Filtro por categoría: "Artesanías" → funciona correctamente

**Pasos:**
1. Navegar a Productos.
2. Buscar "pulsera" por nombre.
3. Buscar "ARE" en el buscador.
4. Buscar código completo "ARE-001".
5. Filtrar por categoría "Artesanías".

**Resultado esperado:** La búsqueda funciona por nombre y código.

**Resultado obtenido:** La búsqueda por nombre y el filtro por categoría funcionan correctamente. Sin embargo, la búsqueda **no encuentra productos por código** — al buscar "ARE" o "ARE-001" no retorna resultados. El buscador solo filtra por nombre.

---

### CP-A004: US-4 — Registro de movimientos de inventario

| Campo | Valor |
|-------|-------|
| **ID** | CP-A004 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Inventario |
| **Nombre** | US-4: Registrar ingresos de mercadería |
| **Tipo de prueba** | Alcance |
| **Estado** | Parcial |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. Existen productos en el sistema.

**Datos de prueba:**
- Entrada de 10 unidades para "Aretes de plata"

**Pasos:**
1. Navegar a Inventario.
2. Registrar entrada de mercadería.
3. Verificar que el stock aumenta.
4. Intentar ver el historial de movimientos registrados.

**Resultado esperado:** Se pueden registrar ingresos y ver el historial de movimientos.

**Resultado obtenido:** El registro de entradas de mercadería funciona correctamente y el stock se actualiza. Sin embargo, **no existe una opción para ver el historial de movimientos** (entradas y salidas registradas) en el módulo de Inventario.

---

### CP-A005: US-5 — Generación de tiquetes de venta

| Campo | Valor |
|-------|-------|
| **ID** | CP-A005 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Ventas |
| **Nombre** | US-5: Generar tiquetes de venta |
| **Tipo de prueba** | Alcance |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. Existen ventas registradas en el sistema.

**Datos de prueba:**
- Venta existente en el historial.

**Pasos:**
1. Navegar a Ventas → historial de ventas.
2. Seleccionar una venta.
3. Usar opción "Imprimir factura" o "Descargar".

**Resultado esperado:** Se genera el comprobante de venta correctamente.

**Resultado obtenido:** El historial de ventas muestra opciones "Imprimir factura" y "Descargar". El comprobante se generó correctamente con los datos de la venta.

---

### CP-A006: US-6 — Actualización automática del inventario por venta

| Campo | Valor |
|-------|-------|
| **ID** | CP-A006 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Ventas → Inventario |
| **Nombre** | US-6: El inventario se actualiza automáticamente al registrar una venta |
| **Tipo de prueba** | Alcance |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. Existe un producto con stock disponible.

**Datos de prueba:**
- Producto con stock conocido, venta de 1 unidad.

**Pasos:**
1. Anotar stock actual de un producto en Inventario.
2. Crear y confirmar una venta de 1 unidad de ese producto.
3. Verificar el stock en Inventario.

**Resultado esperado:** El stock se reduce automáticamente sin intervención manual.

**Resultado obtenido:** El stock se redujo automáticamente al confirmar la venta. No se requirió ninguna acción manual adicional.

---

### CP-A007: US-7 — Registro de emprendimientos y asociación con emprendedoras

| Campo | Valor |
|-------|-------|
| **ID** | CP-A007 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Emprendimientos → Emprendedoras |
| **Nombre** | US-7: Registrar emprendimientos y asociarlos con emprendedoras |
| **Tipo de prueba** | Alcance |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. Usuario autenticado con permiso Administración.

**Datos de prueba:**
- Emprendedora creada previamente.
- Emprendimiento nuevo asociado a esa emprendedora.

**Pasos:**
1. Crear emprendedora nueva.
2. Crear emprendimiento y asociarlo a la emprendedora.
3. Verificar que el emprendimiento muestra la emprendedora asociada.
4. Editar el emprendimiento y cambiar la emprendedora.

**Resultado esperado:** Los emprendimientos se registran y asocian correctamente con emprendedoras.

**Resultado obtenido:** La creación, asociación y edición de emprendimientos con emprendedoras funcionan correctamente.

---

### CP-A008: US-8 — Consulta y edición de información de asociadas

| Campo | Valor |
|-------|-------|
| **ID** | CP-A008 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Emprendedoras |
| **Nombre** | US-8: Consultar y editar información de emprendedoras |
| **Tipo de prueba** | Alcance |
| **Estado** | Parcial |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. Existen emprendedoras registradas.

**Datos de prueba:**
- Campo teléfono modificado con valor "abc123"

**Pasos:**
1. Navegar a Emprendedoras → editar una emprendedora.
2. Modificar el campo teléfono con letras y números mezclados.
3. Guardar.

**Resultado esperado:** La edición funciona. El campo teléfono solo acepta números.

**Resultado obtenido:** La edición se guardó correctamente. Sin embargo, el campo teléfono **acepta letras**, lo que no es un formato válido para un número de teléfono. Falta validación de formato en el campo teléfono.

---

### CP-A009: US-9 — Visualización del estado del inventario

| Campo | Valor |
|-------|-------|
| **ID** | CP-A009 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Inventario |
| **Nombre** | US-9: Ver estado del inventario e identificar productos con bajo stock |
| **Tipo de prueba** | Alcance |
| **Estado** | Parcial |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. Existen productos con diferentes niveles de stock.

**Datos de prueba:**
- Producto con stock 0 (reducido a 0 durante las pruebas).

**Pasos:**
1. Navegar a Inventario.
2. Verificar que se ve el stock de todos los productos.
3. Buscar indicadores visuales de stock bajo o agotado.

**Resultado esperado:** El inventario muestra el stock actual y destaca visualmente los productos con poco stock.

**Resultado obtenido:** El inventario muestra el stock de todos los productos correctamente. Se pudo reducir el stock de un producto a 0. Sin embargo, **no existe un indicador visual** (color, etiqueta, ícono) para productos con stock bajo o agotado dentro del módulo de Inventario. El Dashboard sí muestra el contador de "Stock Bajo: 0" pero el módulo de Inventario no diferencia visualmente los productos críticos.

---

### CP-A010: US-10 — Reporte de ventas por rango de fechas

| Campo | Valor |
|-------|-------|
| **ID** | CP-A010 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Reportes |
| **Nombre** | US-10: Generar reportes de ventas por rango de fechas |
| **Tipo de prueba** | Alcance |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. Existen ventas registradas en el sistema.

**Datos de prueba:**
- Rango de fechas: incluye 2026-04-03

**Pasos:**
1. Navegar a Reportes.
2. Seleccionar fecha inicio y fecha fin libremente.
3. Generar reporte.

**Resultado esperado:** El reporte muestra solo las ventas del rango seleccionado.

**Resultado obtenido:** Las fechas de inicio y fin son seleccionables libremente. El reporte respetó el rango de fechas y mostró solo las ventas del período seleccionado.

---

### CP-A011: US-11 — Identificación de productos con mayor demanda

| Campo | Valor |
|-------|-------|
| **ID** | CP-A011 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Estadísticas |
| **Nombre** | US-11: Ver productos con mayor y menor demanda |
| **Tipo de prueba** | Alcance |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. Existen ventas registradas con diferentes productos.

**Datos de prueba:**
- N/A

**Pasos:**
1. Navegar a Estadísticas.
2. Verificar sección de productos más/menos vendidos.
3. Verificar sección de emprendimientos por ingresos.

**Resultado esperado:** Se muestran los productos más y menos vendidos con métricas de cantidad.

**Resultado obtenido:** Estadísticas muestra: productos más vendidos y menos vendidos con cantidad vendida, emprendimientos con gráfico de ingresos, e indicador de productos con stock bajo al final de la página.

---

### CP-A012: US-12 — Reportes por emprendimiento

| Campo | Valor |
|-------|-------|
| **ID** | CP-A012 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Reportes |
| **Nombre** | US-12: Filtrar reportes por emprendimiento |
| **Tipo de prueba** | Alcance |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. Existen emprendimientos registrados con ventas.

**Datos de prueba:**
- Filtro por emprendimiento específico.

**Pasos:**
1. Navegar a Reportes.
2. Seleccionar un emprendimiento específico en el filtro.
3. Generar el reporte.

**Resultado esperado:** El reporte muestra solo las ventas del emprendimiento seleccionado.

**Resultado obtenido:** El módulo de Reportes permite filtrar por emprendimiento. El reporte mostró correctamente solo los datos del emprendimiento seleccionado.

---

### CP-A013: US-13 — Gestión de cuentas de usuario

| Campo | Valor |
|-------|-------|
| **ID** | CP-A013 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Usuarios |
| **Nombre** | US-13: Crear, editar y eliminar cuentas de usuario |
| **Tipo de prueba** | Alcance |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. Usuario autenticado con permiso Administración.

**Datos de prueba:**
- Usuario creado: ventas@test.com, admin@test.com

**Pasos:**
1. Crear usuarios con diferentes permisos (probado en CP-M005 y CP-I002).
2. Editar usuario ventas@test.com — modificar un dato.
3. Verificar lista de usuarios.

**Resultado esperado:** CRUD completo de usuarios funciona incluyendo asignación de permisos.

**Resultado obtenido:** La creación, edición y visualización de usuarios funcionan correctamente. Los permisos se aplican correctamente al iniciar sesión.

---

### CP-A014: US-14 — Gestión por local

| Campo | Valor |
|-------|-------|
| **ID** | CP-A014 |
| **Fecha** | 2026-04-03 |
| **Módulo** | — |
| **Nombre** | US-14: Gestionar información de diferentes locales |
| **Tipo de prueba** | Alcance |
| **Estado** | No implementado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. La aplicación está ejecutándose.

**Datos de prueba:**
- N/A

**Pasos:**
1. Revisar todos los módulos del menú buscando gestión de locales.

**Resultado esperado:** Existe un módulo para gestionar locales o puntos de venta.

**Resultado obtenido:** No existe ningún módulo ni sección para gestión de locales en la interfaz. La User Story US-14 no está implementada en esta versión.

---

### CP-A015: US-15 — Gestión del contenido del sitio web

| Campo | Valor |
|-------|-------|
| **ID** | CP-A015 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Asociación |
| **Nombre** | US-15: Gestionar contenido mostrado en la página web |
| **Tipo de prueba** | Alcance |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. Usuario autenticado con permiso Administración.

**Datos de prueba:**
- N/A

**Pasos:**
1. Navegar a Asociación.
2. Verificar si existe sección para gestionar contenido web.

**Resultado esperado:** Existe funcionalidad para gestionar el contenido del sitio web.

**Resultado obtenido:** En la sección de Asociación existe una subsección de "Carruseles Web" que permite subir imágenes para mostrar en el sitio web. La funcionalidad de gestión de contenido web está disponible.

---

### CP-A016: US-16 — Destacar productos en la página principal

| Campo | Valor |
|-------|-------|
| **ID** | CP-A016 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Productos |
| **Nombre** | US-16: Marcar productos como destacados para la página web |
| **Tipo de prueba** | Alcance |
| **Estado** | Fallido |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. Existen productos en el sistema.

**Datos de prueba:**
- Cualquier producto existente.

**Pasos:**
1. Navegar a Productos.
2. Localizar el botón o toggle para marcar producto como destacado.
3. Activarlo.

**Resultado esperado:** El producto se marca como destacado y esto se refleja en la página web.

**Resultado obtenido:** El botón para marcar producto como destacado existe en la interfaz, pero **no funciona** — al presionarlo no se realiza ninguna acción visible ni se guarda el cambio.
