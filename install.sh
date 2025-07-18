#!/bin/bash

echo "📦 Creating virtual environment..."
python3 -m venv venv

echo "✅ Activating virtual environment..."
source venv/bin/activate

echo "⬇️ Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "🎉 Installation complete."

echo "To use the tool:"

echo "#source venv/bin/activate"
echo "#python3 qr_g3n.py"
