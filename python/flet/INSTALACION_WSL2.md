¡Lo logramos! WSL2 es una herramienta increíble, pero como es una instalación mínima de Linux, hay que "enseñarle" a manejar gráficos.

Aquí tienes el **Manual Definitivo para WSL2 (Ubuntu)** actualizado al estándar de 2026, con todas las librerías corregidas y el código moderno.

---

# 💻 Guía Definitiva: Flet + Android APK en WSL2 (Ubuntu)

Este manual te permite desarrollar en Windows usando la potencia de Linux, ver la app como una ventana nativa y compilar APKs.

## 1. Sistema y Java (Paquetes Esenciales)
Instalamos la base del sistema y el JDK de Java que te funcionó perfectamente.

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y default-jre default-jdk python3-full python3-pip git curl unzip xz-utils libglu1-mesa chromium-browser
```

## 2. Librerías Gráficas (El "Secreto" de WSL2)
Este paso es el que evita los errores de `.so`. Instala todas las dependencias necesarias para que el cliente de escritorio de Flet funcione en Windows (WSLg).

```bash
sudo apt install -y \
    libmpv-dev libmpv2 libsecret-1-0 libnotify4 \
    libcanberra-gtk3-module libgtk-3-0 libdbus-1-3 liblzma5 \
    libayatana-appindicator3-1 libgstapp-1.0-0 gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good gstreamer1.0-plugins-bad
```

## 3. Instalación de SDKs (Flutter y Android)
Configuramos los motores de desarrollo en tu carpeta personal.

### A. Flutter SDK
```bash
cd ~
git clone https://github.com/flutter/flutter.git -b stable
```

### B. Android SDK (Manual)
```bash
mkdir -p ~/android-sdk/cmdline-tools
cd ~/android-sdk
wget https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip
unzip commandlinetools-linux-*.zip -d cmdline-tools
mv cmdline-tools/cmdline-tools cmdline-tools/latest
rm commandlinetools-linux-*.zip
```

## 4. Configuración del PATH (Variables de Entorno)
Copia y pega este bloque para que Ubuntu reconozca los comandos en cualquier carpeta:

```bash
cat << 'EOF' >> ~/.bashrc

# Configuración Flet & Android en WSL
export ANDROID_HOME=$HOME/android-sdk
export PATH=$PATH:$HOME/flutter/bin
export PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bin
export PATH=$PATH:$ANDROID_HOME/platform-tools
export PATH=$PATH:$ANDROID_HOME/build-tools/36.0.0
export CHROME_EXECUTABLE=/usr/bin/chromium-browser
EOF

source ~/.bashrc
```

## 5. Vinculación y Licencias
Le decimos a Flutter dónde está el SDK y aceptamos los términos de Google.

```bash
flutter config --android-sdk ~/android-sdk
sdkmanager "platform-tools" "platforms;android-36" "build-tools;36.0.0" "build-tools;28.0.3"
yes | flutter doctor --android-licenses
```

## 6. Tu primer proyecto (Estándar 2026)
Crea tu entorno virtual e instala Flet.

```bash
mkdir -p ~/proyectos/mi_app && cd ~/proyectos/mi_app
python3 -m venv .venv
source .venv/bin/activate
pip install flet flet-desktop flet-web
```

Crea el archivo `main.py` con el código actualizado:

```python name=main.py
import flet as ft

def main(page: ft.Page):
    page.title = "App Flet 2026"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    texto = ft.Text("¡Flet funcionando en WSL!", size=30)
    
    def cambiar(e):
        texto.value = "¡Todo configurado correctamente!"
        page.update()

    page.add(
        ft.Row([texto], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.Button("Clic aquí", on_click=cambiar)], alignment=ft.MainAxisAlignment.CENTER)
    )

if __name__ == "__main__":
    ft.run(main)
```

---

## 7. Comandos de Uso Diario en WSL2

| Objetivo | Comando |
| :--- | :--- |
| **Ver app como ventana (Windows)** | `flet run main.py` |
| **Ver app en el navegador** | `flet run --web --port 8001` |
| **Generar APK para Android** | `flet build apk` |

---

### Notas Finales para WSL:
1.  **Rendimiento:** `flet run` en WSL2 usa la GPU de Windows (vía WSLg), por lo que es casi tan rápido como una app nativa.
2.  **Ubicación de archivos:** Te recomiendo siempre trabajar dentro de carpetas de Ubuntu (como `~/proyectos`) y no en carpetas montadas de Windows (como `/mnt/c/`), ya que la compilación de Android es mucho más rápida así.
3.  **Actualizaciones:** Si en el futuro instalas otra versión de Ubuntu y te falta una librería, recuerda que el comando `ldd` sobre el binario de Flet te dirá exactamente qué archivo `.so` falta.

¡Felicidades! Ya tienes el entorno de desarrollo móvil más potente dentro de tu propia computadora.