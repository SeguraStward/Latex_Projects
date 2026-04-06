# Documentación de Pruebas — Inventario del Valle

**Proyecto evaluado:** Inventario del Valle  
**Ejecutado por:** Angel Segura Méndez  
**Fecha:** 2026-04-03  
**Curso:** Ingeniería en Sistemas III — I Ciclo 2026  
**Universidad Nacional, Sede Regional Brunca**  
**Profesor:** Master Saray Castro Mora

---

## Entorno de pruebas

| Componente | Detalle |
|------------|---------|
| Sistema Operativo | Linux Ubuntu |
| Node.js | v22.16.0 |
| Base de datos | SQLite (better-sqlite3) |
| Electron | v36.9.2 |
| Rama del repositorio | `Migracion_SQLITE` |
| Commit evaluado | `f7bde67` |
| Usuario de prueba | test@inventario.local / test123 |

---

## Archivos de casos de prueba

| Archivo | Tipo | Casos |
|---------|------|-------|
| [CP-unitarias.md](CP-unitarias.md) | Pruebas Unitarias | CP-U001 a CP-U010 |
| [CP-modulares.md](CP-modulares.md) | Pruebas Modulares | CP-M001 a CP-M009 |
| [CP-integrales.md](CP-integrales.md) | Pruebas Integrales | CP-I001 a CP-I008 |
| [CP-alcance.md](CP-alcance.md) | Pruebas de Alcance (User Stories) | CP-A001 a CP-A016 |
| [resumen-hallazgos.md](resumen-hallazgos.md) | Hallazgos y Bugs | HAL-001 a HAL-007 |

---

## Resumen de resultados

| Tipo | Total | Aprobados | Parciales | Fallidos | No implementado | Observación |
|------|-------|-----------|-----------|----------|-----------------|-------------|
| Unitarias | 10 | 8 | 0 | 0 | 0 | 1 (CP-U006) |
| Modulares | 9 | 8 | 0 | 1 | 0 | 0 |
| Integrales | 8 | 8 | 0 | 0 | 0 | 0 |
| Alcance (US) | 16 | 9 | 3 | 2 | 1 | 0 |
| **Total** | **43** | **33** | **3** | **3** | **1** | **1** |

---

## Resumen de hallazgos

| ID | Severidad | Descripción breve |
|----|-----------|-------------------|
| HAL-001 | Alta | Producto inactivo sigue visible en módulo de Ventas |
| HAL-002 | Media | Buscador de productos no filtra por código |
| HAL-003 | Alta | No existe historial de movimientos de inventario |
| HAL-004 | Media | No hay indicador visual de stock bajo en Inventario |
| HAL-005 | Baja | Campo teléfono en Emprendedoras acepta letras |
| HAL-006 | Media | US-14 (Gestión por local) no implementada |
| HAL-007 | Alta | Botón "Destacar producto" no funciona |

---

## Módulos evaluados

| # | Módulo | Estado general |
|---|--------|---------------|
| 1 | Autenticación | ✓ Funcional |
| 2 | Dashboard | ✓ Funcional |
| 3 | Productos | ⚠ Funcional con hallazgos (HAL-001, HAL-002, HAL-007) |
| 4 | Categorías | ✓ Funcional |
| 5 | Inventario | ⚠ Funcional con hallazgos (HAL-003, HAL-004) |
| 6 | Ventas | ✓ Funcional |
| 7 | Estadísticas | ✓ Funcional |
| 8 | Reportes | ✓ Funcional |
| 9 | Emprendimientos | ✓ Funcional |
| 10 | Emprendedoras | ⚠ Funcional con hallazgo (HAL-005) |
| 11 | Usuarios y Permisos | ✓ Funcional |
| 12 | Actividades | ✓ Funcional |
| 13 | Asociación | ✓ Funcional |
| 14 | Backup | ✓ Funcional |
| 15 | Sincronización | ✓ Funcional |
| 16 | Gestión de Locales | ✗ No implementado (HAL-006) |
