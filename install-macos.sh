#!/bin/bash

# MiERP Installation Script for macOS
# Usage: bash install-macos.sh

set -e

echo "🍎 MiERP Installation for macOS"
echo "================================"
echo ""

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo "🍺 Homebrew not found. Installing..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

echo "📊 macOS detected"
sw_vers

echo ""
echo "🔄 Step 1: Update Homebrew..."
brew update -q
echo "✅ Done"

echo ""
echo "📦 Step 2: Install system dependencies..."
echo "   Installing: python@3.12, postgresql, git..."
brew install -q python@3.12 postgresql git
echo "✅ Done"

echo ""
echo "🚀 Step 3: Start PostgreSQL..."
brew services start postgresql > /dev/null 2>&1 || true
sleep 2
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
if createdb -l | grep -q mierp_dev; then
    echo "⚠️  Database 'mierp_dev' already exists"
else
    createdb mierp_dev
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
echo "💡 If PostgreSQL is not running, start it with:"
echo "   brew services start postgresql"
echo ""
