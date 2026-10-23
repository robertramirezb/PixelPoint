# PixelPoint

Aplicación de escritorio para Windows que permite detectar y copiar las coordenadas del cursor al hacer clic en cualquier lugar de la pantalla.

## Características

- **Detección global de clics:** captura la posición del cursor incluso cuando estás usando otras aplicaciones.
- **Visualización de coordenadas:** muestra las posiciones `X` e `Y` en una ventana flotante.
- **Copiar al portapapeles:** copia las coordenadas con un solo clic, en el formato `X, Y`.
- **Ventana siempre visible:** mantiene PixelPoint por encima de otras ventanas.
- **Cierre rápido:** permite cerrar la aplicación pulsando la tecla `Esc`.
- **Icono personalizado:** utiliza el archivo `logo.ico`.
- **Ejecutable independiente:** puede distribuirse como un archivo `.exe` generado con PyInstaller.

## Requisitos

Para ejecutar el código fuente:

- Windows 10 o Windows 11.
- Python instalado.
- PyQt6.
- pynput.
- PyInstaller (solo para generar el ejecutable).

## Estructura del proyecto

```text
PixelPoint/
├── main.py
├── interfaz.py
├── controlador.py
├── README.md
├── assets/
│   └── logo.ico
├── build/
└── dist/
    └── PixelPoint.exe
```

> Las carpetas `build/` y `dist/` se generan al compilar el proyecto.

## Instalación para desarrollo

Abre PowerShell en la carpeta del proyecto y ejecuta:

```powershell
python -m pip install PyQt6 pynput pyinstaller
```

## Ejecutar desde el código fuente

```powershell
cd E:\PixelPoint
python main.py
```

## Generar el ejecutable

Desde la carpeta `E:\PixelPoint`, ejecuta:

```powershell
python -m PyInstaller --noconfirm --clean --onefile --windowed --name PixelPoint --icon "assets\logo.ico" --add-data "assets;assets" main.py
```

Al finalizar la compilación, el ejecutable estará en:

```text
E:\PixelPoint\dist\PixelPoint.exe
```

Puedes abrir `PixelPoint.exe` directamente sin ejecutar manualmente `main.py`.

## Cómo utilizar PixelPoint

1. Abre `PixelPoint.exe`.
2. Haz clic en cualquier punto de la pantalla.
3. Consulta las coordenadas mostradas en la ventana.
4. Pulsa **Copiar coordenadas** para copiarlas al portapapeles.
5. Pega las coordenadas donde las necesites.
6. Pulsa `Esc` para cerrar la aplicación.

### Formato de las coordenadas

Las coordenadas se muestran y copian con este formato:

```text
X: 640    Y: 360
```

Al copiar, el contenido del portapapeles será:

```text
640, 360
```

Los valores son píxeles relativos al sistema de coordenadas de la pantalla que reporta el sistema operativo.

## Tecnologías utilizadas

- **Python:** lógica principal de la aplicación.
- **PyQt6:** interfaz gráfica.
- **pynput:** detección global del ratón y el teclado.
- **PyInstaller:** empaquetado del programa como ejecutable para Windows.

## Solución de problemas

### El icono no aparece

Comprueba que el archivo exista en:

```text
E:\PixelPoint\assets\logo.ico
```

Después, vuelve a generar el ejecutable.

### No se detectan los clics

Comprueba que la aplicación se haya iniciado correctamente y que ninguna restricción de seguridad impida capturar los eventos globales del ratón.

### El ejecutable no inicia

Ejecuta el programa desde PowerShell para revisar posibles errores de compilación o dependencias. Para obtener más información, genera temporal