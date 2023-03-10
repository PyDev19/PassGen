import sys

from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtQml import QQmlApplicationEngine

from backend import Backend

app = QGuiApplication(sys.argv)
app.setWindowIcon(QIcon(r"icon.ico"))

backend = Backend()

engine = QQmlApplicationEngine()
engine.rootContext().setContextProperty("backend", backend)
engine.quit.connect(app.quit)
engine.load('gui.qml')

sys.exit(app.exec())
