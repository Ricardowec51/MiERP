# MiERP - Sistema ERP Personalizado

**Licencia**: MIT | **Estado**: ✅ Listo para desarrollo | **Versión Odoo**: 19.0 (master)

## Descripción Rápida

**MiERP** es un sistema ERP empresarial completo basado en Odoo 19.0 (rama master) con todos los módulos estándar incluidos. Diseñado para ser personalizado mediante módulos propios en `custom_addons/`. Todo el código está versionado en GitHub y listo para desarrollo continuo con Claude Code.

## Quick Start para Claude Code

### 1️⃣ Configuración del Ambiente (Primera Vez)

```bash
# Eliminar venv anterior si existe
rm -rf venv

# Crear venv con Python 3.12 (IMPORTANTE: usar 3.12, no 3.14)
/opt/homebrew/opt/python@3.12/bin/python3.12 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### 2️⃣ Iniciar Odoo (Desarrollo Local)

```bash
source venv/bin/activate

# Primera ejecución: crear BD y cargar módulos base
python -m odoo -d mierp_dev -i base

# Ejecuciones posteriores: solo iniciar
python -m odoo -d mierp_dev
```

**Accede a**: http://localhost:8069 (Usuario: admin / Contraseña: admin)

### 3️⃣ Crear Módulo Personalizado

```bash
source venv/bin/activate

# Crear scaffold del módulo
python -m odoo.cli.scaffold mi_modulo custom_addons

# Editar custom_addons/mi_modulo/__manifest__.py
# Luego instalar en Odoo (Apps -> Update List -> Instalar módulo)
```

## Stack Tecnológico

| Componente | Versión | Notas |
|-----------|---------|-------|
| **Odoo** | 19.0 (master) | Rama oficial de desarrollo |
| **Python** | 3.12.12 | ✅ Instalado y configurado |
| **PostgreSQL** | 12+ | Requiere instalación local |
| **Base de Datos** | mierp_dev | Crear con: `createdb mierp_dev` |
| **Licencia** | MIT | Máxima libertad |

## Estructura del Proyecto

```
MiERP/
├── venv/                          # Virtual environment (Python 3.12)
├── custom_addons/                 # 🚀 TUS MÓDULOS PERSONALIZADOS
│   └── (crear módulos aquí)
├── addons/                        # Módulos estándar de Odoo (no tocar)
├── odoo/                          # Core de Odoo (no tocar)
├── requirements.txt               # Dependencias Python
├── LICENSE                        # Licencia MIT
├── README.md                       # Guía de usuario
├── SETUP.md                        # Guía de instalación detallada
├── CLAUDE.md                       # Este archivo (para Claude Code)
├── odoo.conf                       # Configuración de Odoo (crear manualmente)
└── .git/                           # Repositorio Git (GitHub: Ricardowec51/MiERP)
```

## Configuración del Ambiente (Detallado)

### Requisitos del Sistema
- **Python**: 3.12+ (⚠️ NO usar 3.14, tiene incompatibilidades)
- **PostgreSQL**: 12+ instalado y corriendo
- **macOS/Linux/Windows**: Compatible
- **Git**: Para versionado y push a GitHub

## Crear Archivo de Configuración Odoo

Si no existe `odoo.conf`, crear uno:

```bash
cat > odoo.conf << 'EOF'
[options]
# Database
db_host = localhost
db_port = 5432
db_user = postgres
db_password = 
database = mierp_dev

# Addons
addons_path = addons,custom_addons

# Server
admin_passwd = admin
http_port = 8069
workers = 0

# Logging
log_level = info
EOF
```

## Módulos Disponibles (Todos Incluidos)

✅ **Contabilidad**: accounting, invoice, payment, tax, assets
✅ **Ventas**: sale, sale_stock, sale_management
✅ **CRM**: crm, mail, calendar
✅ **Compras**: purchase, purchase_stock
✅ **Inventario**: stock, stock_account, mrp
✅ **RRHH**: hr, hr_contract, hr_payroll
✅ **Proyectos**: project, project_enterprise
✅ **Sitio Web**: website, website_sale, website_form
✅ **Otros**: base, web, auth, settings, etc.

## Desarrollo de Módulos Personalizados

### Crear Nuevo Módulo

```bash
source venv/bin/activate
python -m odoo.cli.scaffold nombre_modulo custom_addons
```

### Estructura Estándar

```
custom_addons/mi_modulo/
├── __init__.py              # Importar models
├── __manifest__.py          # Metadata (nombre, versión, dependencias)
├── models/
│   ├── __init__.py
│   └── model.py            # Tu modelo ORM
├── views/
│   ├── views.xml           # Vistas (form, tree, search)
│   └── menu.xml            # Menús
├── security/
│   └── ir.model.access.csv # Permisos
├── static/
│   └── src/
│       ├── css/
│       ├── js/
│       └── xml/
├── controllers/
│   ├── __init__.py
│   └── main.py            # Rutas HTTP
├── tests/
│   ├── __init__.py
│   └── test_model.py      # Tests
└── README.md              # Documentación del módulo
```

### Instalación en Odoo

1. Crear/editar módulo en `custom_addons/`
2. Iniciar Odoo: `python -m odoo -d mierp_dev`
3. Ir a Aplicaciones → Actualizar lista de aplicaciones
4. Buscar y instalar tu módulo

## Workflow de Desarrollo con Claude Code

### Crear Nueva Feature
```bash
# 1. Crear rama
git checkout -b feature/nueva-funcionalidad

# 2. Crear/editar módulos en custom_addons/
# (Claude Code hace los cambios)

# 3. Probar localmente en http://localhost:8069

# 4. Commit
git add .
git commit -m "Add: descripción de cambios"

# 5. Push a GitHub
git push origin feature/nueva-funcionalidad
```

## Reglas Importantes

⚠️ **NUNCA**:
- Modificar `odoo/` (core de Odoo)
- Modificar `addons/` estándar
- Usar Python < 3.12 o > 3.13

✅ **SIEMPRE**:
- Crear módulos en `custom_addons/`
- Documentar cambios en commits
- Versionear en GitHub
- Testear localmente antes de push

## Recursos

- 📖 [Docs Odoo](https://www.odoo.com/documentation/)
- 🔗 [GitHub: odoo/odoo](https://github.com/odoo/odoo)
- 👥 [OCA Community](https://github.com/OCA/)
- 💾 **Este proyecto**: [GitHub: Ricardowec51/MiERP](https://github.com/Ricardowec51/MiERP)

## Troubleshooting

| Problema | Solución |
|----------|----------|
| `greenlet` error | Usar Python 3.12 (no 3.14) |
| PostgreSQL no conecta | `brew services start postgresql` |
| Puerto 8069 ocupado | Cambiar en `odoo.conf`: `http_port = 8070` |
| Módulo no aparece | Ir a Apps → Actualizar lista → Buscar módulo |
| Cambios en JS no aplican | Limpiar cache: CTRL+SHIFT+R (navegador) |

---

**Estado del Proyecto**:
- ✅ Ambiente configurado: Python 3.12 + Odoo 19.0
- ✅ Repositorio GitHub: Ricardowec51/MiERP
- ✅ Listo para desarrollo con Claude Code
- 📅 **Última actualización**: 2026-05-11 13:30 UTC
- 🎯 **Objetivo**: Desarrollo iterativo de módulos personalizados
