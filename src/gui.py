from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QLineEdit, QLabel, QCheckBox, QPushButton
from PySide6.QtGui import QIcon, QIntValidator
from src.backend import Backend
import sys

class GUI(QMainWindow):
    def __init__(self, app: QApplication):
        super().__init__()
        # Creates style steel
        self.style_sheet = None
        self.add_style()
        
        # Adds style sheet to window
        self.setStyleSheet(self.style_sheet)
        
        # Set title and icon of window
        self.setWindowTitle("PassGen")
        self.setWindowIcon(QIcon("images/icon.ico"))
        
        # Get screen size
        self.app = app
        screen = self.app.primaryScreen()
        screen_size = screen.size()

        # Calculate window x and y position
        x = screen_size.width() / 2 - 600 / 2
        y = screen_size.height() / 2 - 400 / 2
        
        # Set geometery of window
        self.setGeometry(int(x), int(y), 600, 400)
        # Set size of window to be fixed
        self.setFixedSize(600, 400)
        
        # Initialize Backend
        self.backend = Backend()
        
        # Create Widgets
        self.create_widgets()
    
    def add_style(self):
        # Reads style.qss file
        with open("styles/style.qss", "r") as file:
            # Stores contents of file in variable
            self.style_sheet = file.read()
    
    def create_widgets(self):
        # Main Frame
        self.main_frame = QFrame(self)
        self.main_frame.setObjectName("mainFrame")
        self.setCentralWidget(self.main_frame)
        
        # Password Output Entry
        self.generated_password = QLineEdit(self.main_frame)
        self.generated_password.setObjectName("generatedPassword")
        self.generated_password.setGeometry(25, 20, 550, 60)
        self.generated_password.setPlaceholderText("Generated Password")
        self.generated_password.setReadOnly(True)
        
        # Password Lenght Label
        self.pass_len_label = QLabel(self.main_frame)
        self.pass_len_label.setObjectName("passwordLenghtPassword")
        self.pass_len_label.setGeometry(25, 112, 240, 25)
        self.pass_len_label.setText("Password Lenght:")
        
        # Password Lenght Entry
        self.pass_len_label_entry = QLineEdit(self.main_frame)
        self.pass_len_label_entry.setObjectName("passwordLenghtPasswordEntry")
        self.pass_len_label_entry.setGeometry(280, 100, 125, 50)
        self.pass_len_label_entry.setPlaceholderText("10 to 32")
        self.pass_len_label_entry.setValidator(QIntValidator(10, 32))
        
        # Lower Case Characters Checkbox
        self.locase_checkbox = QCheckBox(self.main_frame)
        self.locase_checkbox.setText("Lower Case Characters")
        self.locase_checkbox.setGeometry(25, 180, 350, 25)
        
        # Upper Case Characters Checkbox
        self.upcase_checkbox = QCheckBox(self.main_frame)
        self.upcase_checkbox.setText("Upper Case Characters")
        self.upcase_checkbox.setGeometry(25, 240, 350, 25)
        
        # Special Characters Checkbox
        self.spchar_checkbox = QCheckBox(self.main_frame)
        self.spchar_checkbox.setText("Special Characters")
        self.spchar_checkbox.setGeometry(25, 300, 350, 25)
        
        # Generate Password Button
        self.generate_password_btn = QPushButton(self.main_frame)
        self.generate_password_btn.setText("Generate Password")
        self.generate_password_btn.setGeometry(100, 340, 400, 50)
        self.generate_password_btn.clicked.connect(lambda: self.generate_password())
        
    def generate_password(self):
        lenght = int(self.pass_len_label_entry.text())
        locase = self.locase_checkbox.isChecked()
        upcase = self.upcase_checkbox.isChecked()
        spchar = self.spchar_checkbox.isChecked()
        
        password = self.backend.generate_password(lenght, locase, upcase, spchar)
        self.generated_password.setText(password)
        
        password = None
        lenght = None
        locase = None
        upcase = None
        spchar = None
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = GUI()
    window.show()
    
    sys.exit(app.exec())

