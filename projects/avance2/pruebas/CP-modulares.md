# Pruebas Modulares — Inventario del Valle

**Ejecutado por:** Angel Segura Méndez  
**Fecha:** 2026-04-03  
**Tipo:** Pruebas Modulares (interrelación entre módulos)  
**Rama evaluada:** `Migracion_SQLITE`  
**Usuario de prueba:** test@inventario.local / test123

---

### CP-M001: Categoría creada es asignable a producto

| Campo | Valor |
|-------|-------|
| **ID** | CP-M001 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Categorías → Productos |
| **Nombre** | Categoría creada aparece disponible al crear producto |
| **Tipo de prueba** | Modular |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. La aplicación está ejecutándose.
2. Usuario autenticado con test@inventario.local / test123.

**Datos de prueba:**
- Categoría: nombre `Artesanías`, código `ART-001`

**Pasos:**
1. Navegar a "Categorías" → nueva categoría.
2. Ingresar nombre "Artesanías" y código "ART-001".
3. Guardar la categoría.
4. Navegar a "Productos" → nuevo producto.
5. Verificar que la categoría "Artesanías" aparece en el selector.

**Resultado esperado:** La categoría recién creada aparece disponible en el formulario de producto.

**Resultado obtenido:** La categoría "Artesanías" ya existía en el sistema. Al ingresar un código nuevo el sistema la actualizó (código único). Al ir a Productos, la categoría sí apareció disponible en el selector. El sistema previene duplicados por código correctamente.

---

### CP-M002: Emprendedora creada es asociable a emprendimiento

| Campo | Valor |
|-------|-------|
| **ID** | CP-M002 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Emprendedoras → Emprendimientos |
| **Nombre** | Emprendedora creada aparece disponible al crear emprendimiento |
| **Tipo de prueba** | Modular |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. La aplicación está ejecutándose.
2. Usuario autenticado.

**Datos de prueba:**
- Nueva emprendedora con nombre, apellidos, cédula y correo.

**Pasos:**
1. Navegar a "Emprendedoras" → nueva emprendedora.
2. Ingresar datos y guardar.
3. Navegar a "Emprendimientos" → nuevo emprendimiento.
4. Verificar que la emprendedora creada aparece en el selector.

**Resultado esperado:** La emprendedora recién creada está disponible para asociar al emprendimiento.

**Resultado obtenido:** La emprendedora creada apareció disponible en el formulario de emprendimientos correctamente.

---

### CP-M003: Venta registrada reduce stock automáticamente (US-6)

| Campo | Valor |
|-------|-------|
| **ID** | CP-M003 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Ventas → Inventario |
| **Nombre** | Registrar venta descuenta stock del producto |
| **Tipo de prueba** | Modular |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. La aplicación está ejecutándose.
2. Existe producto "Pulsera Artesanal" con stock 20.

**Datos de prueba:**
- Producto: Pulsera Artesanal, stock inicial: 20
- Cantidad vendida: 7

**Pasos:**
1. Verificar stock inicial en "Inventario": Pulsera Artesanal = 20.
2. Navegar a "Ventas" → nueva venta.
3. Agregar "Pulsera Artesanal" con cantidad 7.
4. Confirmar la venta.
5. Volver a "Inventario" y verificar nuevo stock.

**Resultado esperado:** Stock pasa de 20 a 13 automáticamente.

**Resultado obtenido:** El stock se redujo de 20 a 13 correctamente. La interrelación Ventas → Inventario funciona.

---

### CP-M004: Ingreso de mercadería aumenta stock (US-4)

| Campo | Valor |
|-------|-------|
| **ID** | CP-M004 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Inventario (movimientos) → Stock |
| **Nombre** | Registrar entrada de mercadería aumenta el stock |
| **Tipo de prueba** | Modular |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. Producto "Pulsera Artesanal" con stock 13 (resultado de CP-M003).

**Datos de prueba:**
- Producto: Pulsera Artesanal
- Tipo movimiento: Entrada
- Cantidad: 10

**Pasos:**
1. Navegar a "Inventario" → registrar entrada.
2. Seleccionar "Pulsera Artesanal", cantidad 10.
3. Confirmar el movimiento.
4. Verificar nuevo stock.

**Resultado esperado:** Stock sube de 13 a 23.

**Resultado obtenido:** El stock subió correctamente de 13 a 23. El módulo de movimientos de inventario actualiza el stock correctamente.

---

### CP-M005: Usuario con rol "Ventas" no accede a módulos administrativos

| Campo | Valor |
|-------|-------|
| **ID** | CP-M005 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Usuarios → Permisos → Navegación |
| **Nombre** | Control de acceso: rol Ventas solo ve módulos autorizados |
| **Tipo de prueba** | Modular |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. La aplicación está ejecutándose.

**Datos de prueba:**
- Usuario nuevo: ventas@test.com / test123
- Permisos: solo "Ventas"

**Pasos:**
1. Crear usuario ventas@test.com con solo permiso "Ventas".
2. Cerrar sesión.
3. Iniciar sesión con ventas@test.com / test123.
4. Observar el menú lateral.

**Resultado esperado:** Solo aparecen los módulos de ventas: Inicio, Inventario, Ventas, Estadísticas, Reportes.

**Resultado obtenido:** El menú mostró exactamente 5 secciones: Inicio, Inventario, Ventas, Estadísticas y Reportes. Los módulos Usuarios, Productos, Categorías, Emprendimientos, Emprendedoras, Actividades y Asociación no son visibles.

---

### CP-M006: Producto inactivo sigue visible en módulo de ventas

| Campo | Valor |
|-------|-------|
| **ID** | CP-M006 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Productos → Ventas |
| **Nombre** | Producto inactivo no debería estar disponible para venta |
| **Tipo de prueba** | Modular |
| **Estado** | Fallido |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. La aplicación está ejecutándose.
2. Existe un producto activo en el sistema.

**Datos de prueba:**
- Producto marcado como inactivo.

**Pasos:**
1. Navegar a "Productos" → editar un producto → cambiar estado a inactivo.
2. Navegar a "Ventas" → nueva venta.
3. Buscar el producto inactivo.

**Resultado esperado:** El producto inactivo NO aparece disponible para seleccionar en ventas.

**Resultado obtenido:** El producto inactivo SÍ aparece disponible en el selector de ventas. **Hallazgo de bug:** el filtro de productos activos no se aplica en el módulo de ventas.

---

### CP-M007: Reporte filtra ventas por rango de fechas (US-10)

| Campo | Valor |
|-------|-------|
| **ID** | CP-M007 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Ventas → Reportes |
| **Nombre** | Reporte muestra ventas del rango de fechas seleccionado |
| **Tipo de prueba** | Modular |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. Existen ventas registradas hoy (2026-04-03) por las pruebas anteriores.

**Datos de prueba:**
- Rango de fechas: incluye 2026-04-03

**Pasos:**
1. Navegar a "Reportes".
2. Seleccionar rango de fechas que incluya hoy.
3. Generar reporte.

**Resultado esperado:** El reporte incluye las ventas realizadas hoy durante las pruebas.

**Resultado obtenido:** Las ventas realizadas durante las pruebas aparecieron correctamente en el reporte del periodo seleccionado.

---

### CP-M008: Estadísticas muestran productos más vendidos (US-11)

| Campo | Valor |
|-------|-------|
| **ID** | CP-M008 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Ventas → Estadísticas |
| **Nombre** | Estadísticas reflejan productos vendidos |
| **Tipo de prueba** | Modular |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. Existen ventas registradas en el sistema.

**Datos de prueba:**
- Producto vendido: Pulsera Artesanal (7 unidades en CP-M003)

**Pasos:**
1. Navegar a "Estadísticas".
2. Verificar si aparece "Pulsera Artesanal" como producto vendido.

**Resultado esperado:** Estadísticas reflejan la venta de Pulsera Artesanal.

**Resultado obtenido:** "Pulsera Artesanal" apareció en estadísticas correctamente. El módulo refleja las ventas realizadas.

---

### CP-M009: Sincronización exitosa con Supabase

| Campo | Valor |
|-------|-------|
| **ID** | CP-M009 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Sincronización → Supabase |
| **Nombre** | Sincronización con página web se ejecuta correctamente |
| **Tipo de prueba** | Modular |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. La aplicación está ejecutándose.
2. Usuario tiene permiso de sincronización.
3. Conexión a internet disponible.

**Datos de prueba:**
- N/A

**Pasos:**
1. Localizar el botón de sincronización (barra superior).
2. Presionar el botón de sincronización.
3. Observar el mensaje resultante.

**Resultado esperado:** El sistema indica que la sincronización fue exitosa.

**Resultado obtenido:** El sistema mostró el mensaje: "la sincronización con la página web fue exitosa". La interrelación entre el sistema local y Supabase funciona correctamente.
