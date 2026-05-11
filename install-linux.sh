#!/bin/bash

# MiERP Installation Script for Linux (Ubuntu 24.04 / Debian 13+)
# Usage: bash install-linux.sh

set -e

echo "🐧 MiERP Installation for Linux"
echo "================================"
echo ""

# Detect Linux distribution
if [ -f /etc/os-release ]; then
    . /etc/os-release
    OS=$ID
    VERSION=$VERSION_ID
else
    echo "❌ Cannot detect Linux distribution"
    exit 1
fi

echo "📊 Detected: $OS $VERSION"

# Check if Ubuntu 24.04 or Debian 13+
if [[ "$OS" != "ubuntu" && "$OS" != "debian" ]]; then
    echo "⚠️  This script is tested on Ubuntu 24.04 and Debian 13+"
    echo "⚠️  Your system: $OS $VERSION"
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    [[ ! $REPLY =~ ^[Yy]$ ]] && exit 1
fi

echo ""
echo "🔄 Step 1: Update system packages..."
sudo apt update -qq
echo "✅ Done"

echo ""
echo "📦 Step 2: Install system dependencies..."
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
    zlib1g-dev \
    > /dev/null 2>&1
echo "✅ Done"

echo ""
echo "🚀 Step 3: Start PostgreSQL..."
sudo systemctl start postgresql
sudo systemctl enable postgresql
echo "✅ Done"

echo ""
echo "📁 Step 4: Create virtual environment..."
if [ ! -d "venv" ]; then
    python3.12 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "⚠️  Virtual environment already exists"
fi

echo ""
echo "📚 Step 5: Activate venv and install dependencies..."
source venv/bin/activate
pip install --upgrade pip setuptools wheel > /dev/null 2>&1
pip install -r requirements.txt > /dev/null 2>&1
echo "✅ Dependencies installed"

echo ""
echo "🗄️  Step 6: Create PostgreSQL database..."
if sudo -u postgres psql -lqt | cut -d \| -f 1 | grep -qw mierp_dev; then
    echo "⚠️  Database 'mierp_dev' already exists"
else
    sudo -u postgres psql -c "CREATE DATABASE mierp_dev;"
    echo "✅ Database 'mierp_dev' created"
fi

echo ""
echo "✅ Installation completed successfully!"
echo ""
echo "🚀 To start Odoo:"
echo "   1. source venv/bin/activate"
echo "   2. python -m odoo -d mierp_dev -i base"
echo "   3. Open http://localhost:8069"
echo "   4. Login: admin / admin"
echo ""
