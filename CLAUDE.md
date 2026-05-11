# MiERP - Sistema ERP Personalizado

## Descripción del Proyecto

**MiERP** es un sistema ERP completo basado en Odoo que incluye todos los módulos estándar, diseñado para ser personalizado y adaptado a necesidades específicas de negocio.

### Objetivos
- Proporcionar una base sólida de ERP con todos los módulos de Odoo
- Permitir el desarrollo de módulos personalizados específicos del negocio
- Mantener la compatibilidad con actualizaciones futuras de Odoo
- Licencia MIT para máxima flexibilidad

## Stack Tecnológico
- **Base**: Odoo (rama master)
- **Lenguaje**: Python
- **Base de datos**: PostgreSQL
- **Frontend**: Odoo Web Framework / JavaScript
- **Licencia**: MIT

## Estructura del Proyecto

```
MiERP/
├── addons/                 # Módulos personalizados de MiERP
├── odoo/                   # Core de Odoo (no modificar)
├── addons/                 # Módulos estándar de Odoo
├── LICENSE                 # Licencia MIT
├── README.md               # Información del proyecto
└── CLAUDE.md               # Este archivo
```

## Configuración del Ambiente

### Requisitos Previos
- Python 3.10+
- PostgreSQL 12+
- pip y virtualenv

### Instalación Inicial

```bash
cd MiERP

# Crear entorno virtual
python -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Crear base de datos
createdb mierp_dev

# Inicializar Odoo
python -m odoo -d mierp_dev -i base
```

## Módulos Disponibles

Se incluyen todos los módulos estándar de Odoo en el directorio `addons/`:
- **Contabilidad**: accounting, invoice, payment
- **CRM**: crm, sales
- **Inventario**: stock, purchase
- **Recursos Humanos**: hr, recruitment, payroll
- **Proyecto**: project, tasks
- **Sitio Web**: website, e-commerce
- Y muchos más...

## Desarrollo de Módulos Personalizados

Los módulos personalizados irán en:
```
MiERP/custom_addons/
```

### Estructura de un Módulo Personalizado
```
custom_addons/mi_modulo/
├── __init__.py
├── __manifest__.py
├── models/
├── views/
├── security/
├── static/
└── wizard/
```

## Workflow de Desarrollo

1. Crear rama para nueva feature/módulo
2. Desarrollar módulo personalizado en `custom_addons/`
3. Probar con instancia local de Odoo
4. Crear pull request para revisión
5. Merge a master una vez aprobado

## Consideraciones Importantes

- **No modificar** el directorio `odoo/` (es el core de Odoo)
- Los módulos personalizados van siempre en `custom_addons/`
- Mantener compatibilidad con versiones de Odoo
- Documentar módulos personalizados en sus respectivos README.md
- Usar Python y JavaScript estándar de Odoo

## Recursos Útiles

- [Documentación Oficial de Odoo](https://www.odoo.com/documentation/)
- [Repositorio GitHub de Odoo](https://github.com/odoo/odoo)
- [Comunidad OCA (Odoo Community Association)](https://github.com/OCA/)

## Contacto y Contribuciones

Para contribuciones, issues o sugerencias, abre un issue en el repositorio.

---

**Última actualización**: 2026-05-11
