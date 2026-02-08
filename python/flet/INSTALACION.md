
---

# 🚀 Manual Maestro: Flet + Android APK en Debian Remoto (2026)

Este manual sirve para configurar un servidor "headless" (sin monitor) en Vultr para desarrollar aplicaciones multiplataforma y compilar APKs de Android.

## 1. Preparación del Sistema y Java (Ajustado)
Primero actualizamos el sistema e instalamos las dependencias base. Usamos los paquetes por defecto de Debian para asegurar compatibilidad total.

```bash
sudo apt update && sudo apt upgrade -y
# Instalación de Java y herramientas de sistema
sudo apt install -y default-jre default-jdk python3-full python3-pip git curl unzip xz-utils libglu1-mesa chromium
```

## 2. Instalación de Flutter SDK
Descargamos el motor de Flutter en tu carpeta personal.

```bash
cd ~
git clone https://github.com/flutter/flutter.git -b stable
```

## 3. Instalación del Android SDK (Command Line Tools)
Instalamos solo las herramientas de consola para mantener el servidor ligero.

```bash
mkdir -p ~/android-sdk/cmdline-tools
cd ~/android-sdk

# Descarga de herramientas oficiales
wget https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip
unzip commandlinetools-linux-*.zip -d cmdline-tools

# IMPORTANTE: Re-estructurar carpetas para que Flutter las reconozca
mv cmdline-tools/cmdline-tools cmdline-tools/latest
rm commandlinetools-linux-*.zip
```

## 4. Configuración de Variables de Entorno (PATH)
Copia y pega este bloque completo para que el sistema reconozca todos los comandos nuevos:

```bash
cat << 'EOF' >> ~/.bashrc

# Flutter & Android SDK Config
export ANDROID_HOME=$HOME/android-sdk
export PATH=$PATH:$HOME/flutter/bin
export PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bin
export PATH=$PATH:$ANDROID_HOME/platform-tools
export PATH=$PATH:$ANDROID_HOME/build-tools/36.0.0
export CHROME_EXECUTABLE=/usr/bin/chromium
EOF

source ~/.bashrc
```

## 5. Instalación de Componentes de Android y Licencias
Configuramos las versiones exactas que tu versión de Flutter requiere para compilar APKs.

```bash
# Vincular Flutter con el SDK manual
flutter config --android-sdk ~/android-sdk

# Instalar las plataformas y herramientas requeridas (v36 y v28.0.3)
sdkmanager "platform-tools" "platforms;android-36" "build-tools;36.0.0" "build-tools;28.0.3"

# Aceptar todas las licencias de Android (Indispensable)
yes | flutter doctor --android-licenses
```

## 6. Configuración del Proyecto Flet (Python)
Entramos a la carpeta de tu app y configuramos el entorno virtual.

```bash
mkdir -p ~/proyectos/mi_app && cd ~/proyectos/mi_app
python3 -m venv .venv
source .venv/bin/activate

# Instalar Flet y sus módulos necesarios para evitar errores de importación
pip install flet flet-desktop flet-web
```

---

## 7. Guía de Uso Diario

### A. Para probar tu app (Modo Web)
Como estás en un servidor remoto, usa este comando para ver la app desde tu navegador (ej. `http://tu_ip:8001`):
```bash
flet run --web --port 8001 --host 0.0.0.0 -d
```

### B. Para generar el APK de Android
Asegúrate de tener tu código en la carpeta `src/main.py` y luego ejecuta:
```bash
flet build apk
```
*El archivo final estará en: `build/apk/app-release.apk`*

---

## 💡 Recordatorios de Mantenimiento

- **Verificación de estado**: Si algo falla, el comando `flutter doctor` es tu mejor amigo. Te dirá exactamente qué falta.
- **Túneles/Puertos**: Si usas un túnel para el puerto 8001, asegúrate de que el túnel esté apuntando a la IP `0.0.0.0` del servidor.
- **Java**: Si alguna vez actualizas el servidor y Java deja de responder, verifica con `java -version` que el paquete `default-jdk` sigue activo.
