# MiERP - Sistema ERP Completo

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Odoo Master](https://img.shields.io/badge/Odoo-Master-orange.svg)

## 📋 Descripción

**MiERP** es un sistema ERP empresarial completo y personalizable basado en **Odoo**. Incluye todos los módulos estándar de Odoo con soporte completo para:

- ✅ Contabilidad e Invoicing
- ✅ Gestión de Ventas (CRM)
- ✅ Gestión de Compras
- ✅ Inventario y Almacén
- ✅ Recursos Humanos
- ✅ Proyectos y Tareas
- ✅ Sitio Web y E-commerce
- ✅ Y mucho más...

## 🚀 Inicio Rápido

### Requisitos
- Python 3.10+
- PostgreSQL 12+
- pip y virtualenv
- Git

### Instalación

```bash
# Clonar y acceder al proyecto
cd MiERP

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Crear base de datos
createdb mierp_dev

# Ejecutar Odoo
python -m odoo -d mierp_dev -i base
```

Luego accede a `http://localhost:8069`

## 📁 Estructura del Proyecto

```
MiERP/
├── addons/              # Módulos estándar de Odoo
├── odoo/                # Core de Odoo (no modificar)
├── custom_addons/       # 🔧 TU ESPACIO: Módulos personalizados
├── LICENSE              # Licencia MIT
├── CLAUDE.md            # Documentación técnica
└── README.md            # Este archivo
```

## 🔧 Desarrollo de Módulos Personalizados

Los módulos personalizados van en **`custom_addons/`**:

```bash
# Crear nuevo módulo personalizado
mkdir -p custom_addons/mi_modulo/{models,views,security,static}

# Crear __init__.py
touch custom_addons/mi_modulo/__init__.py

# Crear __manifest__.py
cat > custom_addons/mi_modulo/__manifest__.py << 'MANIFEST'
{
    'name': 'Mi Módulo',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Tu Nombre',
    'installable': True,
}
MANIFEST
```

## 📚 Documentación

- Ver **[CLAUDE.md](./CLAUDE.md)** para detalles técnicos y arquitectura
- Documentación oficial: https://www.odoo.com/documentation/
- Comunidad OCA: https://github.com/OCA/

## 📝 Licencia

Este proyecto está bajo licencia **MIT**. Ver [LICENSE](./LICENSE) para más detalles.

## 🤝 Contribuciones

1. Crea una rama para tu feature: `git checkout -b feature/mi-feature`
2. Commit tus cambios: `git commit -m 'Add mi-feature'`
3. Push a la rama: `git push origin feature/mi-feature`
4. Abre un Pull Request

## ⚠️ Notas Importantes

- **No modificar** el directorio `odoo/` - es el core de Odoo
- **No modificar** el directorio `addons/` - son módulos estándar
- Usa siempre `custom_addons/` para tus desarrollos personalizados
- Documenta tus módulos con un README.md en cada uno

## 📞 Soporte

Para reportar bugs o solicitar features, abre un issue en el repositorio.

---

**Última actualización**: 2026-05-11
**Versión de Odoo**: Master (última)
**Estado**: 🟢 Activo en desarrollo
