import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QLineEdit, QPushButton, QVBoxLayout

class HauptFenster(QWidget):
    def __init__(self):
        super().__init__()
        #sample(layout)
        self.name_field = QLineEdit()
        self.button1 = QPushButton('Beenden')
        self.button2 = QPushButton('Weiter')
        
        layout = QVBoxLayout()
        layout.addWidget(self.name_field)

        buttons = QHBoxLayout()
        buttons.addWidget(self.button1)
        buttons.addWidget(self.button2)
        layout.addLayout(buttons)        

        self.setLayout(layout)
        #end-sample
        self.setWindowTitle('Name eingeben')
        self.setFixedSize(300, 100)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HauptFenster()
    window.show()
    sys.exit(app.exec())