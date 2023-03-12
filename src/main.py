from src.gui import GUI
from PySide6.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
    
window = GUI(app)
window.show()

sys.exit(app.exec())
