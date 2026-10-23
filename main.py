
import sys
from pathlib import Path

from PyQt6.QtWidgets import QApplication

from interfaz import VentanaCoordenadas
from controlador import ControladorCoordenadas


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("PixelPoint")

    # Buscar el icono tanto al ejecutar Python como el .exe
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        carpeta_base = Path(sys._MEIPASS)
    else:
        carpeta_base = Path(__file__).resolve().parent

    ruta_icono = carpeta_base / "assets" / "logo.ico"

    if ruta_icono.exists():
        from PyQt6.QtGui import QIcon
        app.setWindowIcon(QIcon(str(ruta_icono)))

    ventana = VentanaCoordenadas()
    controlador = ControladorCoordenadas(ventana)

    # Centrar la ventana en la pantalla
    pantalla = app.primaryScreen()
    if pantalla:
        area = pantalla.availableGeometry()
        x = area.x() + (area.width() - ventana.width()) // 2
        y = area.y() + (area.height() - ventana.height()) // 2
        ventana.move(x, y)

    # Detener los listeners al salir de la aplicación
    app.aboutToQuit.connect(controlador.detener)

    ventana.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
