#!/bin/bash

echo "📦 Creating virtual environment..."
python3 -m venv venv

echo "✅ Activating virtual environment..."
source venv/bin/activate

echo "⬇️ Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "🎉 Installation complete. \r\n"

echo "To use the tool: \r\n"

echo "#source venv/bin/activate \r\n"
echo "#python3 qr_g3n.py \r\n"
