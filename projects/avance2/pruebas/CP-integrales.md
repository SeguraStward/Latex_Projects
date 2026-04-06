# Pruebas Integrales — Inventario del Valle

**Ejecutado por:** Angel Segura Méndez  
**Fecha:** 2026-04-03  
**Tipo:** Pruebas Integrales (flujos end-to-end)  
**Rama evaluada:** `Migracion_SQLITE`  
**Usuario de prueba:** test@inventario.local / test123

---

### CP-I001: Flujo completo — crear producto y venderlo

| Campo | Valor |
|-------|-------|
| **ID** | CP-I001 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Categorías → Productos → Inventario → Ventas |
| **Nombre** | Flujo completo de creación de producto hasta venta |
| **Tipo de prueba** | Integral |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. La aplicación está ejecutándose.
2. Usuario autenticado con test@inventario.local / test123.

**Datos de prueba:**
- Categoría: Bisutería, código BIS-001
- Producto: Aretes de plata, código ARE-001, precio ₡2500
- Entrada de stock: 10 unidades
- Venta: 2 unidades

**Pasos:**
1. Crear categoría "Bisutería" (código BIS-001).
2. Crear producto "Aretes de plata" asociado a categoría "Bisutería", precio ₡2500.
3. Intentar vender sin stock — observar respuesta del sistema.
4. Registrar entrada de 10 unidades en Inventario.
5. Crear venta de 2 unidades de "Aretes de plata".
6. Verificar stock final en Inventario.

**Resultado esperado:** Stock final = 8 (10 entrada - 2 venta). Sistema bloquea venta sin stock.

**Resultado obtenido:** Al intentar vender con stock 0, el sistema mostró error "stock insuficiente para el movimiento". Luego de registrar 10 unidades de entrada, la venta de 2 unidades se completó correctamente. Stock final = 8. Flujo completo funcionó correctamente.

---

### CP-I002: Flujo completo — crear usuario, asignar permisos y verificar acceso

| Campo | Valor |
|-------|-------|
| **ID** | CP-I002 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Usuarios → Permisos → Autenticación → Navegación |
| **Nombre** | Flujo completo de gestión de usuario con permisos |
| **Tipo de prueba** | Integral |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. La aplicación está ejecutándose.
2. Usuario administrador autenticado.

**Datos de prueba:**
- Usuario: Ana Prueba, correo admin@test.com, contraseña test123
- Permiso asignado: solo Administración

**Pasos:**
1. Navegar a "Usuarios" → crear nuevo usuario con datos indicados.
2. Asignar solo permiso "Administración".
3. Guardar usuario.
4. Cerrar sesión.
5. Iniciar sesión con admin@test.com / test123.
6. Verificar módulos disponibles en el menú.

**Resultado esperado:** El menú muestra solo módulos administrativos (Inicio, Productos, Categorías, Emprendimientos, Emprendedoras, Actividades, Asociación). No muestra Ventas, Estadísticas ni Reportes.

**Resultado obtenido:** El menú mostró exactamente 7 módulos: Inicio, Productos, Categorías, Emprendimientos, Emprendedoras, Actividades y Asociación. Los módulos de ventas no aparecieron. El sistema aplicó correctamente los permisos asignados.

---

### CP-I003: Flujo completo — generación y exportación de reporte PDF

| Campo | Valor |
|-------|-------|
| **ID** | CP-I003 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Ventas → Reportes → PDF |
| **Nombre** | Generación y exportación de reporte de ventas en PDF |
| **Tipo de prueba** | Integral |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. La aplicación está ejecutándose.
2. Existen ventas registradas en el sistema.

**Datos de prueba:**
- Rango de fechas: incluye 2026-04-03

**Pasos:**
1. Navegar a "Reportes".
2. Seleccionar rango de fechas que incluya hoy.
3. Generar el reporte.
4. Exportar a PDF.

**Resultado esperado:** El PDF se genera correctamente con los datos de ventas del período.

**Resultado obtenido:** El reporte se generó y el PDF se exportó correctamente.

---

### CP-I004: Flujo completo — crear actividad/taller

| Campo | Valor |
|-------|-------|
| **ID** | CP-I004 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Actividades |
| **Nombre** | Crear actividad y verificar que aparece en la lista |
| **Tipo de prueba** | Integral |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. La aplicación está ejecutándose.
2. Usuario autenticado.

**Datos de prueba:**
- Título: Taller de tejido
- Tipo: Taller
- Fecha inicio: 2026-04-03

**Pasos:**
1. Navegar a "Actividades" → nueva actividad.
2. Ingresar título "Taller de tejido", tipo y fecha inicio.
3. Guardar.
4. Verificar que aparece en la lista de actividades.

**Resultado esperado:** La actividad "Taller de tejido" aparece en la lista.

**Resultado obtenido:** La actividad se creó y apareció correctamente en la lista de actividades.

---

### CP-I005: Flujo completo — editar producto e intento de eliminación con registros asociados

| Campo | Valor |
|-------|-------|
| **ID** | CP-I005 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Productos |
| **Nombre** | Editar producto y verificar protección de integridad al eliminar |
| **Tipo de prueba** | Integral |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. Existe el producto "Aretes de plata" con ventas asociadas.

**Datos de prueba:**
- Producto: Aretes de plata
- Nuevo precio: ₡3000

**Pasos:**
1. Navegar a "Productos" → editar "Aretes de plata".
2. Cambiar precio a ₡3000.
3. Guardar.
4. Verificar que el precio se actualizó en la lista.
5. Intentar eliminar "Aretes de plata".

**Resultado esperado:** La edición funciona. La eliminación falla con mensaje de error por registros asociados.

**Resultado obtenido:** El precio se actualizó correctamente a ₡3000. Al intentar eliminar, el sistema mostró: "no se puede eliminar porque tiene registros asociados". La integridad referencial funciona correctamente.

---

### CP-I006: Flujo completo — edición de información de la Asociación

| Campo | Valor |
|-------|-------|
| **ID** | CP-I006 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Asociación |
| **Nombre** | Editar y guardar información de la asociación |
| **Tipo de prueba** | Integral |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. La aplicación está ejecutándose.
2. Existe información de la asociación cargada.

**Datos de prueba:**
- Campo editado: Misión (texto modificado)

**Pasos:**
1. Navegar a "Asociación".
2. Verificar que hay información cargada.
3. Editar el campo de Misión.
4. Guardar los cambios.
5. Verificar que el cambio persiste.

**Resultado esperado:** La información se actualiza y persiste correctamente.

**Resultado obtenido:** Había información cargada en el módulo. El cambio en la misión se guardó correctamente.

---

### CP-I007: Flujo completo — búsqueda y filtro de productos

| Campo | Valor |
|-------|-------|
| **ID** | CP-I007 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Productos |
| **Nombre** | Búsqueda por nombre y filtro por categoría funcionan correctamente |
| **Tipo de prueba** | Integral |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. Existen productos en el sistema, incluyendo "Pulsera Artesanal".
2. Existe la categoría "Artesanías" con productos asociados.

**Datos de prueba:**
- Búsqueda: "pulsera"
- Filtro por categoría: Artesanías

**Pasos:**
1. Navegar a "Productos".
2. Buscar por texto "pulsera".
3. Verificar resultados.
4. Filtrar por categoría "Artesanías".
5. Verificar resultados del filtro.

**Resultado esperado:** La búsqueda y el filtro muestran solo los productos que coinciden.

**Resultado obtenido:** Tanto la búsqueda por nombre "pulsera" como el filtro por categoría "Artesanías" funcionaron correctamente, mostrando solo los productos correspondientes.

---

### CP-I008: Flujo completo — backup de la base de datos

| Campo | Valor |
|-------|-------|
| **ID** | CP-I008 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Backup |
| **Nombre** | Generación de respaldo de la base de datos SQLite |
| **Tipo de prueba** | Integral |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. La aplicación está ejecutándose.
2. Usuario autenticado con permisos suficientes.

**Datos de prueba:**
- Carpeta de destino seleccionada por el usuario.

**Pasos:**
1. Localizar la opción de Backup en el menú.
2. Ejecutar el backup.
3. Seleccionar carpeta de destino.
4. Verificar que el archivo se generó.

**Resultado esperado:** El sistema genera el archivo de respaldo de la base de datos SQLite en la carpeta seleccionada.

**Resultado obtenido:** El sistema solicitó la carpeta de destino y generó el respaldo de la base de datos SQLite correctamente.
