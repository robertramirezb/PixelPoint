
from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtWidgets import QApplication

from pynput import mouse, keyboard


class ControladorCoordenadas(QObject):
    clic_detectado = pyqtSignal(int, int)
    cerrar_solicitado = pyqtSignal()

    def __init__(self, ventana):
        super().__init__()

        self.ventana = ventana
        self.ultima_x = None
        self.ultima_y = None

        # Conectar señales con métodos de la ventana/controlador
        self.clic_detectado.connect(self.actualizar_coordenadas)
        self.cerrar_solicitado.connect(self.ventana.close)
        self.ventana.copiar_solicitado.connect(
            self.copiar_coordenadas
        )

        # Escuchar los clics globales del ratón
        self.listener_mouse = mouse.Listener(
            on_click=self.al_hacer_clic
        )

        # Escuchar la tecla Escape globalmente
        self.listener_teclado = keyboard.Listener(
            on_press=self.al_presionar_tecla
        )

        self.listener_mouse.start()
        self.listener_teclado.start()

    def al_hacer_clic(self, x, y, boton, presionado):
        """Detecta la posición cuando se presiona un botón del ratón."""
        if presionado:
            self.clic_detectado.emit(int(x), int(y))

    def al_presionar_tecla(self, tecla):
        """Cierra PixelPoint al presionar Escape."""
        if tecla == keyboard.Key.esc:
            self.cerrar_solicitado.emit()
            return False

    def actualizar_coordenadas(self, x, y):
        """Guarda y muestra las últimas coordenadas."""
        self.ultima_x = x
        self.ultima_y = y
        self.ventana.mostrar_coordenadas(x, y)

    def copiar_coordenadas(self):
        """Copia las últimas coordenadas al portapapeles."""
        if self.ultima_x is None or self.ultima_y is None:
            return

        texto = f"{self.ultima_x}, {self.ultima_y}"
        QApplication.clipboard().setText(texto)
        self.ventana.mostrar_copiado()

    def detener(self):
        """Detiene los listeners al cerrar la aplicación."""
        if self.listener_mouse.is_alive():
            self.listener_mouse.stop()

        if self.listener_teclado.is_alive():
            self.listener_teclado.stop()
