# MiERP — Módulos Personalizados

## 🎯 Visión General

MiERP incluye **9 módulos personalizados** basados en Odoo 19.0, creados específicamente para satisfacer las necesidades de un sistema ERP profesional, con soporte para **múltiples idiomas** (Español, English, Português Brasil).

---

## 📦 Módulos Disponibles

### 1. **mierp_base** (Secuencia: 1)
**Base del sistema y configuración**

- **Propósito**: Módulo fundacional que todos los demás heredan
- **Modelos**:
  - `res.company` (extensión) — Campos MiERP personalizados
- **Características**:
  - Menú raíz "MiERP" en la barra principal
  - Configuración de branding
  - Campos: `mierp_version`, `mierp_brand_name`, `mierp_module_enabled`
- **Dependencias**: `base`, `mail`
- **i18n**: es, en, pt_BR

---

### 2. **mierp_sale** (Secuencia: 10)
**Gestión de Ventas y CRM**

- **Modelos**:
  - `sale.order` (extensión) — Órdenes de venta personalizadas
  - `crm.lead` (extensión) — Oportunidades y leads
- **Características**:
  - Menú: MiERP > Ventas > Pedidos / Oportunidades
  - Campos adicionales: canal de venta, prioridad de lead, fuente de oportunidad
  - Vistas list/form extendidas
- **Dependencias**: `mierp_base`, `sale`, `crm`
- **Menú**: Ventas, Pedidos de Venta, Oportunidades
- **i18n**: es, en, pt_BR

---

### 3. **mierp_purchase** (Secuencia: 20)
**Gestión de Compras**

- **Modelos**:
  - `purchase.order` (extensión) — Órdenes de compra
  - `res.partner` (extensión) — Información de proveedores
- **Características**:
  - Menú: MiERP > Compras > Órdenes
  - Campos: tipo de compra, calificación de proveedor, código de proveedor
- **Dependencias**: `mierp_base`, `purchase`
- **i18n**: es, en, pt_BR

---

### 4. **mierp_inventory** (Secuencia: 30)
**Gestión de Inventario y Almacén**

- **Modelos**:
  - `product.template` (extensión) — Productos personalizados
  - `stock.picking` (extensión) — Movimientos de stock
- **Características**:
  - Menú: MiERP > Inventario > Productos / Movimientos
  - Campos: SKU personalizado, ubicación de almacenamiento, nivel de reorden
  - Control de stock avanzado
- **Dependencias**: `mierp_base`, `stock`
- **i18n**: es, en, pt_BR

---

### 5. **mierp_accounting** (Secuencia: 40)
**Gestión Contable y Financiera**

- **Modelos**:
  - `account.move` (extensión) — Asientos contables y facturas
  - `account.journal` (extensión) — Diarios contables
- **Características**:
  - Menú: MiERP > Contabilidad > Facturas / Pagos
  - Campos: tipo de documento, referencia personalizada, departamento
  - Reportes financieros personalizados
- **Dependencias**: `mierp_base`, `account`
- **i18n**: es, en, pt_BR

---

### 6. **mierp_hr** (Secuencia: 50)
**Recursos Humanos y Nómina**

- **Modelos**:
  - `hr.employee` (extensión) — Empleados con campos custom
  - `hr.payslip` (extensión) — Nóminas personalizadas
- **Características**:
  - Menú: MiERP > RRHH > Empleados / Nóminas
  - Campos: código de empleado, tipo de empleo, método de pago
  - Gestión de contratos y beneficios
- **Dependencias**: `mierp_base`, `hr`, `hr_payroll`
- **i18n**: es, en, pt_BR

---

### 7. **mierp_project** (Secuencia: 60)
**Gestión de Proyectos y Tareas**

- **Modelos**:
  - `project.project` (extensión) — Proyectos personalizados
  - `project.task` (extensión) — Tareas del proyecto
- **Características**:
  - Menú: MiERP > Proyectos > Proyectos / Tareas
  - Campos: código de proyecto, prioridad, tipo de tarea, horas estimadas
  - Seguimiento de tiempo y avance
- **Dependencias**: `mierp_base`, `project`
- **i18n**: es, en, pt_BR

---

### 8. **mierp_helpdesk** (Secuencia: 70)
**Sistema de Soporte y Tickets**

- **Modelos**:
  - `mierp.helpdesk.ticket` (nuevo) — Tickets de soporte propios
    - Hereda de `mail.thread` para mensajería
- **Características**:
  - Menú: MiERP > Soporte > Tickets
  - Campos: número de ticket, cliente, asignado a, estado, prioridad
  - Estados: New > Open > In Progress > Pending > Closed / Cancelled
  - Vistas: lista, form (con statusbar)
  - Búsqueda por estado
- **Dependencias**: `mierp_base`, `mail`
- **i18n**: es, en, pt_BR

---

### 9. **mierp_portal** (Secuencia: 80)
**Portal de Cliente y Website**

- **Modelos**:
  - `mierp.portal.config` (nuevo) — Configuración del portal
- **Características**:
  - Menú: Settings > Portal > Configuración
  - Campos: nombre del portal, tema personalizado, análisis
  - Descripción del portal para acceso público
  - Integración con website
- **Dependencias**: `mierp_base`, `portal`, `website`
- **i18n**: es, en, pt_BR

---

## 🌐 Soporte Multiidioma

Cada módulo incluye traducción completa para:

| Idioma | Código | Archivos |
|--------|--------|----------|
| **Español** | `es` | `i18n/es.po` |
| **English** | `en` | `i18n/en.po` |
| **Português (Brasil)** | `pt_BR` | `i18n/pt_BR.po` |

Archivos adicionales:
- `i18n/[module].pot` — Template de traducción

### Cómo cambiar idioma en Odoo:
1. Settings > Users > Language
2. Seleccionar idioma deseado
3. Recargar página

---

## 📊 Estructura de Directorios

```
custom_addons/
├── mierp_base/
│   ├── __init__.py
│   ├── __manifest__.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── mierp_base_model.py
│   ├── views/
│   │   ├── menu.xml
│   │   └── mierp_base_views.xml
│   ├── security/
│   │   └── ir.model.access.csv
│   └── i18n/
│       ├── mierp_base.pot
│       ├── es.po
│       ├── en.po
│       └── pt_BR.po
│
├── mierp_sale/      [8 módulos más con estructura similar]
├── mierp_purchase/
├── mierp_inventory/
├── mierp_accounting/
├── mierp_hr/
├── mierp_project/
├── mierp_helpdesk/
└── mierp_portal/
```

---

## 🚀 Instalación de Módulos

### Opción 1: Instalar todos
```bash
source venv/bin/activate
python -m odoo -d mierp_dev \
  -i mierp_base,mierp_sale,mierp_purchase,mierp_inventory,\
     mierp_accounting,mierp_hr,mierp_project,mierp_helpdesk,\
     mierp_portal
```

### Opción 2: Instalar uno por uno
```bash
# Instalar base primero (otros dependen)
python -m odoo -d mierp_dev -i mierp_base

# Luego instalar los demás
python -m odoo -d mierp_dev -i mierp_sale
python -m odoo -d mierp_dev -i mierp_purchase
# ... etc
```

### En la interfaz de Odoo:
1. Ir a **Apps** (Aplicaciones)
2. Buscar "mierp"
3. Hacer clic en **Install** en cada módulo
4. Esperar a que se instale (puede tomar minutos)

---

## 📝 Dependencias Entre Módulos

```
mierp_base
  ↓
  ├─→ mierp_sale (depende de: sale, crm)
  ├─→ mierp_purchase (depende de: purchase)
  ├─→ mierp_inventory (depende de: stock)
  ├─→ mierp_accounting (depende de: account)
  ├─→ mierp_hr (depende de: hr, hr_payroll)
  ├─→ mierp_project (depende de: project)
  ├─→ mierp_helpdesk (depende de: mail)
  └─→ mierp_portal (depende de: portal, website)
```

**Importante**: Instalar siempre `mierp_base` primero.

---

## 🔐 Seguridad

Cada módulo incluye reglas de acceso (`ir.model.access.csv`) definidas por grupo:

- **Base User**: Lectura en la mayoría de modelos
- **System/Admin**: Permisos completos en configuración
- **Grupo específico**: Permisos personalizados según módulo

Personalizar permisos en: Settings > Security > Access Control

---

## 🎨 Personalización

Cada módulo está diseñado para ser **fácilmente extensible**:

### Agregar campos a un modelo:
```python
# En custom_addons/mierp_sale/models/mierp_sale_model.py
class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    mi_nuevo_campo = fields.Char('Mi Campo')
```

### Crear vistas personalizadas:
```xml
<!-- En custom_addons/mierp_sale/views/mierp_sale_views.xml -->
<record id="view_order_custom" model="ir.ui.view">
    <field name="name">sale.order.custom</field>
    <field name="model">sale.order</field>
    <field name="inherit_id" ref="sale.view_order_form"/>
    <field name="arch" type="xml">
        <!-- XML aquí -->
    </field>
</record>
```

---

## 📚 Documentación Relacionada

- `CLAUDE.md` — Guía completa de desarrollo
- `MULTIPLATFORM.md` — Compatibilidad macOS/Linux
- `SETUP.md` — Instalación inicial
- `README.md` — Descripción del proyecto

---

## 📌 Notas Importantes

✅ **Todos los módulos**:
- Siguen convenciones Odoo 19.0
- Usan rutas relativas (compatible macOS + Linux)
- Incluyen seguridad y acceso control
- Soportan 3 idiomas completos
- Tienen vistas list/form básicas
- Heredan de módulos Odoo core

❌ **No incluyen** (lista para desarrollo):
- Reportes avanzados (plantilla base disponible)
- Flujos de trabajo (preparado para workflow)
- Integración API externa (hooks disponibles)
- Gráficos/dashboards (vistas básicas listas)

---

**Estado**: ✅ Completo y listo para desarrollo  
**Última actualización**: 2026-05-11  
**Licencia**: MIT
