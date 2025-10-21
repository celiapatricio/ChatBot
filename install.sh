#!/bin/bash

# Salir si hay error
set -e

echo "[Info-install] Creando entorno virtual."
python3 -m venv .venv

echo "[Info-install] Activando entorno virtual."
source .venv/bin/activate

echo "[Info-install] Actualizando pip."
pip install --upgrade pip

echo "[Info-install] Instalando dependencias."
pip install -r requirements.txt

echo ""
echo "[Info-install] Instalación completada."