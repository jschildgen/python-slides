import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

# sample(name_eingeben)
class HauptFenster(QWidget):
    def __init__(self):
        super().__init__()
        self.name_field = QLineEdit()
        self.button = QPushButton('OK')
        self.button.clicked.connect(self.on_button_click)
        self.result_label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.name_field)
        layout.addWidget(self.button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)
        # end-sample
        self.setWindowTitle('Name eingeben')
        self.setFixedSize(300, 100)

    # sample(button_click)
    def on_button_click(self):
        name = self.name_field.text()
        self.result_label.setText(f'Hallo {name}!')
    # end-sample

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HauptFenster()
    window.show()
    sys.exit(app.exec_())
