# Pruebas Unitarias — Inventario del Valle

**Ejecutado por:** Ange Segura Méndez  
**Fecha:** 2026-04-03  
**Tipo:** Pruebas Unitarias  
**Rama evaluada:** `Migracion_SQLITE`  
**Usuario de prueba:** test@inventario.local / test123

---

### CP-U001: Login exitoso con credenciales válidas

| Campo | Valor |
|-------|-------|
| **ID** | CP-U001 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Autenticación |
| **Nombre** | Login exitoso con credenciales válidas |
| **Tipo de prueba** | Unitaria |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. La aplicación está ejecutándose.
2. El usuario test@inventario.local existe en la base de datos con contraseña test123.

**Datos de prueba:**
- Correo: test@inventario.local
- Contraseña: test123

**Pasos:**
1. Abrir la aplicación.
2. Ingresar correo: test@inventario.local
3. Ingresar contraseña: test123
4. Hacer clic en "Iniciar sesión".

**Resultado esperado:** El sistema autentica al usuario y muestra el Dashboard con el menú lateral completo.

**Resultado obtenido:** La app cargó correctamente. El menú lateral muestra todos los módulos: Inicio, Inventario, Ventas, Estadísticas, Usuarios, Reportes, Productos, Categorías, Emprendimientos, Emprendedoras, Actividades y Asociación.

---

### CP-U002: Login fallido con contraseña incorrecta

| Campo | Valor |
|-------|-------|
| **ID** | CP-U002 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Autenticación |
| **Nombre** | Login fallido — contraseña incorrecta |
| **Tipo de prueba** | Unitaria |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. La aplicación está ejecutándose.
2. El usuario test@inventario.local existe en la base de datos.

**Datos de prueba:**
- Correo: test@inventario.local
- Contraseña: wrongpassword

**Pasos:**
1. Cerrar sesión.
2. Ingresar correo: test@inventario.local
3. Ingresar contraseña: wrongpassword
4. Hacer clic en "Iniciar sesión".

**Resultado esperado:** El sistema muestra un mensaje de error. No redirige al dashboard.

**Resultado obtenido:** El sistema mostró el mensaje: "el usuario o contraseña son incorrectos". No redirigió al dashboard.

---

### CP-U003: Login fallido con correo inexistente

| Campo | Valor |
|-------|-------|
| **ID** | CP-U003 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Autenticación |
| **Nombre** | Login fallido — correo no registrado |
| **Tipo de prueba** | Unitaria |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. La aplicación está ejecutándose.
2. El correo noexiste@test.com NO existe en la base de datos.

**Datos de prueba:**
- Correo: noexiste@test.com
- Contraseña: test123

**Pasos:**
1. Cerrar sesión.
2. Ingresar correo: noexiste@test.com
3. Ingresar contraseña: test123
4. Hacer clic en "Iniciar sesión".

**Resultado esperado:** El sistema muestra un mensaje de error. No redirige al dashboard.

**Resultado obtenido:** El sistema mostró el mensaje: "el usuario o contraseña son incorrectos". No redirigió al dashboard.

---

### CP-U004: Validación de formulario de categoría — campos obligatorios

| Campo | Valor |
|-------|-------|
| **ID** | CP-U004 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Categorías |
| **Nombre** | Validación de campos obligatorios en nueva categoría |
| **Tipo de prueba** | Unitaria |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. La aplicación está ejecutándose.
2. Usuario autenticado con test@inventario.local / test123.

**Datos de prueba:**
- Nombre: _(vacío)_
- Código: _(vacío)_

**Pasos:**
1. Navegar a "Categorías".
2. Hacer clic en "Nueva categoría" (o botón equivalente).
3. Dejar todos los campos vacíos.
4. Intentar guardar.

**Resultado esperado:** El formulario no se envía y muestra indicación de campos requeridos.

**Resultado obtenido:** El formulario mostró mensajes en los campos indicando que son requeridos. No se envió el formulario.

---

### CP-U005: Validación de formulario de producto — precio negativo

| Campo | Valor |
|-------|-------|
| **ID** | CP-U005 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Productos |
| **Nombre** | Validación: precio no puede ser negativo |
| **Tipo de prueba** | Unitaria |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. La aplicación está ejecutándose.
2. Usuario autenticado con test@inventario.local / test123.
3. Existe al menos una categoría y un emprendimiento en el sistema.

**Datos de prueba:**
- Nombre: "Producto Test Negativo"
- Código: "PRD-NEG-01"
- Precio: -500

**Pasos:**
1. Navegar a "Productos".
2. Hacer clic en nuevo producto.
3. Ingresar nombre, código y precio -500.
4. Intentar guardar.

**Resultado esperado:** El sistema rechaza el precio negativo con un mensaje de error.

**Resultado obtenido:** El sistema mostró el mensaje: "intenta agregar un precio de venta válido". No se guardó el producto.

---

### CP-U006: El stock se gestiona en módulo de Inventario, no en Productos

| Campo | Valor |
|-------|-------|
| **ID** | CP-U006 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Productos / Inventario |
| **Nombre** | El stock no se ingresa en el formulario de producto |
| **Tipo de prueba** | Unitaria |
| **Estado** | Observación |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. La aplicación está ejecutándose.
2. Usuario autenticado.

**Datos de prueba:**
- Formulario de creación de nuevo producto.

**Pasos:**
1. Navegar a "Productos" → Nuevo producto.
2. Observar los campos disponibles en el formulario.

**Resultado esperado:** _(exploración del diseño del módulo)_

**Resultado obtenido:** El formulario de productos no incluye un campo de stock. El stock se administra en el módulo de **Inventario** mediante movimientos. Esto corresponde a un diseño correcto: el stock se controla mediante entradas y salidas, no editándolo directamente.

---

### CP-U007: Cálculo de total de venta — un producto

| Campo | Valor |
|-------|-------|
| **ID** | CP-U007 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Ventas |
| **Nombre** | Total de venta calculado correctamente con un producto |
| **Tipo de prueba** | Unitaria |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. La aplicación está ejecutándose.
2. Existe al menos un producto con precio conocido en el sistema.

**Datos de prueba:**
- Producto existente con precio conocido
- Cantidad: 3

**Pasos:**
1. Navegar a "Ventas" → Nueva venta.
2. Seleccionar un producto.
3. Ingresar cantidad 3.
4. Observar el total calculado automáticamente.

**Resultado esperado:** Total = precio unitario × 3.

**Resultado obtenido:** El sistema calculó correctamente. Precio unitario ₡12, cantidad 3, total ₡36.

---

### CP-U008: Logout cierra la sesión correctamente

| Campo | Valor |
|-------|-------|
| **ID** | CP-U008 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Autenticación |
| **Nombre** | Cerrar sesión redirige al login |
| **Tipo de prueba** | Unitaria |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. Usuario autenticado en la aplicación.

**Datos de prueba:**
- N/A

**Pasos:**
1. Hacer clic en el botón de cerrar sesión.
2. Observar si redirige a la pantalla de login.

**Resultado esperado:** La sesión se cierra y la app muestra la pantalla de login.

**Resultado obtenido:** Verificado durante las pruebas CP-U002 y CP-U003 — el logout funcionó correctamente y redirigió al login en ambas ocasiones.

---

### CP-U009: Dashboard carga métricas al iniciar sesión

| Campo | Valor |
|-------|-------|
| **ID** | CP-U009 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Dashboard (Inicio) |
| **Nombre** | Pantalla de inicio carga correctamente |
| **Tipo de prueba** | Unitaria |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. Usuario autenticado.

**Datos de prueba:**
- N/A

**Pasos:**
1. Iniciar sesión.
2. Observar la pantalla de Inicio/Dashboard.
3. Verificar si muestra métricas (ventas, productos, stock bajo, etc.).

**Resultado esperado:** El dashboard muestra métricas del sistema sin errores.

**Resultado obtenido:** El dashboard mostró: Total Productos: 5, Productos Activos: 5, Ventas Mensuales: ₡24,000, Stock Bajo: 0. También mostró sección de acciones rápidas. Sin errores.

---

### CP-U010: Validación de formulario de venta — sin productos

| Campo | Valor |
|-------|-------|
| **ID** | CP-U010 |
| **Fecha** | 2026-04-03 |
| **Módulo** | Ventas |
| **Nombre** | No se puede guardar venta sin productos |
| **Tipo de prueba** | Unitaria |
| **Estado** | Aprobado |
| **Ejecutado por** | Angel Segura Méndez |

**Precondiciones:**
1. La aplicación está ejecutándose.
2. Usuario autenticado.

**Datos de prueba:**
- Formulario de venta vacío (sin productos agregados)

**Pasos:**
1. Navegar a "Ventas" → Nueva venta.
2. No agregar ningún producto.
3. Intentar guardar/confirmar la venta.

**Resultado esperado:** El sistema muestra error indicando que la venta debe tener al menos un producto.

**Resultado obtenido:** El sistema mostró el mensaje: "debemos agregar al menos una venta". No guardó la venta vacía.
