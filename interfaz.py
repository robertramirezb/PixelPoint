
import sys
from pathlib import Path

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
)


class VentanaCoordenadas(QWidget):
    copiar_solicitado = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("PixelPoint")
        self.setFixedSize(290, 165)
        self.setWindowFlags(
            self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint
        )

        # Encontrar el icono en Python y en el ejecutable de PyInstaller
        if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
            carpeta_base = Path(sys._MEIPASS)
        else:
            carpeta_base = Path(__file__).resolve().parent

        ruta_icono = carpeta_base / "assets" / "logo.ico"
        if ruta_icono.exists():
            self.setWindowIcon(QIcon(str(ruta_icono)))

        self.etiqueta_titulo = QLabel("PixelPoint")
        self.etiqueta_titulo.setObjectName("titulo")
        self.etiqueta_titulo.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.etiqueta_coordenadas = QLabel("X: --    Y: --")
        self.etiqueta_coordenadas.setObjectName("coordenadas")
        self.etiqueta_coordenadas.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.boton_copiar = QPushButton("Copiar coordenadas")
        self.boton_copiar.setCursor(
            Qt.CursorShape.PointingHandCursor
        )
        self.boton_copiar.setEnabled(False)
        self.boton_copiar.clicked.connect(
            self.copiar_solicitado.emit
        )

        layout = QVBoxLayout()
        layout.setContentsMargins(16, 12, 16, 12)
        layout.setSpacing(10)
        layout.addWidget(self.etiqueta_titulo)
        layout.addWidget(self.etiqueta_coordenadas)
        layout.addWidget(self.boton_copiar)
        self.setLayout(layout)

        self.setStyleSheet("""
            QWidget {
                background-color: #202124;
                color: #F1F3F4;
                font-family: "Segoe UI", Arial, sans-serif;
                font-size: 10pt;
            }

            QLabel#titulo {
                color: #8AB4F8;
                font-size: 16pt;
                font-weight: bold;
            }

            QLabel#coordenadas {
                background-color: #303134;
                border: 1px solid #5F6368;
                border-radius: 6px;
                padding: 8px;
                font-size: 12pt;
                font-weight: bold;
            }

            QPushButton {
                background-color: #8AB4F8;
                color: #202124;
                border: none;
                border-radius: 6px;
                padding: 8px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #AECBFA;
            }

            QPushButton:pressed {
                background-color: #669DF6;
            }

            QPushButton:disabled {
                background-color: #5F6368;
                color: #BDC1C6;
            }
        """)

    def mostrar_coordenadas(self, x, y):
        """Actualiza las coordenadas que aparecen en la ventana."""
        self.etiqueta_coordenadas.setText(f"X: {x}    Y: {y}")
        self.boton_copiar.setEnabled(True)
        self.boton_copiar.setText("Copiar coordenadas")

    def mostrar_copiado(self):
        """Muestra que las coordenadas se copiaron."""
        self.boton_copiar.setText("¡Copiado!")
