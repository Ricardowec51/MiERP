# Configuración del Ambiente MiERP

## Estado Actual

✅ Entorno virtual creado: venv/
⏳ Instalando dependencias...

## Una vez completada la instalación:

### 1. Crear Base de Datos

#### Opción A: Si tienes PostgreSQL instalado
```
createdb mierp_dev
```

#### Opción B: Si necesitas instalar PostgreSQL (macOS)
```
brew install postgresql
brew services start postgresql
createdb mierp_dev
```

### 2. Crear archivo de configuración (odoo.conf)

Copia esto en un archivo odoo.conf:

```
[options]
db_host = localhost
db_port = 5432
db_user = postgres
db_password = 
database = mierp_dev
addons_path = addons,custom_addons
admin_passwd = admin
http_port = 8069
log_level = info
```

### 3. Iniciar Odoo

```
source venv/bin/activate
python -m odoo -d mierp_dev -i base --config odoo.conf
```

### 4. Acceder

URL: http://localhost:8069
Usuario: admin
Contraseña: admin

## Problemas Comunes

PostgreSQL no disponible:
```
brew services start postgresql
```

Puerto 8069 en uso - cambiar en odoo.conf:
```
http_port = 8070
```

