#!/bin/bash

printf "📦 Creating virtual environment...\n"
python3 -m venv venv

printf "✅ Activating virtual environment...\n"
source venv/bin/activate

printf "⬇ Installing dependencies...\n"
pip install --upgrade pip
pip install --break-system-packages -r requirements.txt

printf "🎉 Installation complete.\n"

