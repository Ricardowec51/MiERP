# MiERP - Instalación Multi-Plataforma

## 🎯 Objetivo Esencial

**MiERP debe ser ejecutable en:**
- ✅ macOS (presente y futuros)
- ✅ Ubuntu 24.04 LTS
- ✅ Debian 13 en adelante

**No usar:** Paths específicas de SO, dependencias exclusivas de plataforma, comandos incompatibles.

---

## 📋 Requisitos Universales

| Componente | Versión | Notas |
|-----------|---------|-------|
| **Python** | 3.12+ (no 3.14) | Disponible en todas las plataformas |
| **PostgreSQL** | 12+ | Base de datos relacional |
| **Git** | 2.30+ | Control de versiones |
| **pip** | Último | Gestor de paquetes Python |

---

## 🐧 Instalación en Linux (Ubuntu 24.04 / Debian 13+)

### 1️⃣ Instalar Dependencias del Sistema

```bash
# Ubuntu 24.04 / Debian 13+
sudo apt update
sudo apt install -y \
    python3.12 \
    python3.12-venv \
    python3.12-dev \
    postgresql \
    postgresql-contrib \
    git \
    build-essential \
    libpq-dev \
    libssl-dev \
    libffi-dev \
    libxml2-dev \
    libxslt1-dev \
    libjpeg-dev \
    zlib1g-dev

# Iniciar PostgreSQL
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

### 2️⃣ Crear Entorno Virtual

```bash
cd /ruta/a/MiERP

# Crear venv con Python 3.12
python3.12 -m venv venv
source venv/bin/activate

# Actualizar pip
pip install --upgrade pip setuptools wheel
```

### 3️⃣ Instalar Dependencias del Proyecto

```bash
pip install -r requirements.txt
```

### 4️⃣ Crear Base de Datos

```bash
# Conectarse a PostgreSQL como usuario postgres
sudo -u postgres psql

# Dentro de psql:
CREATE DATABASE mierp_dev;
\q
```

### 5️⃣ Iniciar Odoo

```bash
source venv/bin/activate
python -m odoo -d mierp_dev -i base
```

**Accede a**: http://localhost:8069

---

## 🍎 Instalación en macOS (Intel / Apple Silicon)

### 1️⃣ Instalar Homebrew (si no lo tienes)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2️⃣ Instalar Dependencias

```bash
brew install python@3.12 postgresql git

# Iniciar PostgreSQL
brew services start postgresql
```

### 3️⃣ Crear Entorno Virtual

```bash
cd /ruta/a/MiERP

# Crear venv con Python 3.12
python3.12 -m venv venv
source venv/bin/activate

# Actualizar pip
pip install --upgrade pip setuptools wheel
```

### 4️⃣ Instalar Dependencias del Proyecto

```bash
pip install -r requirements.txt
```

### 5️⃣ Crear Base de Datos

```bash
# Crear la base de datos
createdb mierp_dev
```

### 6️⃣ Iniciar Odoo

```bash
source venv/bin/activate
python -m odoo -d mierp_dev -i base
```

**Accede a**: http://localhost:8069

---

## 🔄 Comandos Unificados (Funcionan en Ambas Plataformas)

```bash
# Activar entorno virtual
source venv/bin/activate

# Instalar/actualizar dependencias
pip install -r requirements.txt

# Ejecutar Odoo
python -m odoo -d mierp_dev

# Crear módulo
python -m odoo.cli.scaffold nombre_modulo custom_addons

# Control de Git (idéntico en todas)
git status
git add .
git commit -m "mensaje"
git push origin main
```

---

## ⚙️ Diferencias por Plataforma

### Rutas y Variables de Entorno

| Elemento | Linux | macOS |
|----------|-------|-------|
| **Python** | `/usr/bin/python3.12` | `/opt/homebrew/opt/python@3.12/bin/python3.12` |
| **PostgreSQL Start** | `sudo systemctl start postgresql` | `brew services start postgresql` |
| **PostgreSQL User** | `sudo -u postgres` | `whoami` (usuario actual) |
| **Activar venv** | `source venv/bin/activate` | `source venv/bin/activate` (igual) |
| **Path Separator** | `/` | `/` (igual) |

### Consideraciones Especiales

#### En Linux
- Usar `sudo` para comandos de sistema
- PostgreSQL corre como servicio del sistema
- Rutas pueden ser `/home/usuario/...` o `/root/...`

#### En macOS
- No necesita `sudo` para la mayoría de operaciones
- PostgreSQL vía Homebrew es más simple
- Rutas suelen ser `/Users/usuario/...`

---

## 🛡️ Compatibilidad Asegurada

### ✅ Prácticas Implementadas

1. **Rutas Relativas**: Todos los paths son relativos al proyecto
   ```python
   # ❌ MAL
   addons_path = /home/usuario/MiERP/addons
   
   # ✅ BIEN
   addons_path = addons,custom_addons
   ```

2. **Scripts de Shell**: Compatible con bash/zsh
   ```bash
   # ✅ Compatible (bash/zsh)
   source venv/bin/activate
   
   # ❌ NO Compatible (PowerShell)
   .\venv\Scripts\activate
   ```

3. **Dependencias Python**: Cross-platform
   - `requirements.txt` funciona igual en todas
   - Librerías compiladas (lxml, psycopg2) incluyen wheels

4. **Configuración Odoo**: archivos `.conf`
   - Mismo formato en todas las plataformas
   - Usar rutas relativas siempre

---

## 📝 Checklist de Compatibilidad

Antes de mergear código:

- [ ] ¿Usa rutas absolutas? Cambiar a relativas
- [ ] ¿Comandos específicos del SO? Crear equivalentes para ambos
- [ ] ¿Dependencias nativas? Verificar disponibilidad en Linux
- [ ] ¿Scripts bash/shell? Testear en ambas plataformas
- [ ] ¿Rutas hardcodeadas? Usar variables de entorno

---

## 🧪 Testing Multi-Plataforma

### Workflow Sugerido

1. **Desarrollar en macOS/Linux principal**
2. **Antes de commit:**
   ```bash
   # Verificar que funciona localmente
   python -m odoo -d mierp_dev -i base
   
   # Testear en máquina virtual si es posible
   # O documentar diferencias encontradas
   ```
3. **Documentar en PR:**
   - "Testeado en: macOS 14.5 + Ubuntu 24.04"

---

## 🔗 Recursos Útiles

### Linux (Ubuntu/Debian)
- [Odoo en Ubuntu](https://www.odoo.com/documentation/17.0/administration/on_premise.html)
- [PostgreSQL en Debian](https://wiki.debian.org/PostgreSQL)

### macOS
- [Homebrew](https://brew.sh/)
- [Python.org macOS](https://www.python.org/downloads/macos/)

---

## 📌 Notas Importantes

- **Python 3.12 es OBLIGATORIO** en todas las plataformas
- **No usar 3.14** por incompatibilidades
- **PostgreSQL debe estar corriendo** antes de iniciar Odoo
- **Paths relativas siempre** (no rutas absolutas)
- **Git LFS no usado** (repositorio <2GB)

---

**Última actualización**: 2026-05-11
**Estado**: ✅ Verificado multi-plataforma
