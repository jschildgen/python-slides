import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QListWidget

class HauptFenster(QWidget):
    def __init__(self):
        super().__init__()
        # sample(listwidget)
        self.obstauswahl = QListWidget()
        self.obstauswahl.addItem('Apfel')
        self.obstauswahl.addItem('Birne')
        self.obstauswahl.addItem('Mango')
        self.obstauswahl.currentTextChanged.connect(self.on_list_change)
        # end-sample

        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.obstauswahl)
        layout.addWidget(self.label)

        self.setLayout(layout)
        
        self.setWindowTitle('QListWidget')
        self.setFixedSize(200, 100)

    # sample(list_change)
    def on_list_change(self, obst):
        self.label.setText(f'Lecker, {obst}!')
    # end-sample

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HauptFenster()
    window.show()
    sys.exit(app.exec())
