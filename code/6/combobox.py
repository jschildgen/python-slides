import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox

class HauptFenster(QWidget):
    def __init__(self):
        super().__init__()
        # sample(combobox)
        self.obstauswahl = QComboBox()
        self.obstauswahl.addItem('Apfel')
        self.obstauswahl.addItem('Birne')
        self.obstauswahl.addItem('Mango')
        self.obstauswahl.currentIndexChanged.connect(self.on_combo_change)
        # end-sample

        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.obstauswahl)
        layout.addWidget(self.label)

        self.setLayout(layout)
        
        self.setWindowTitle('QComboBox')
        self.setFixedSize(200, 100)

    # sample(combo_change)
    def on_combo_change(self, idx):
        self.label.setText(f'Lecker, {self.obstauswahl.currentText()}!')
        # oder:
        self.label.setText(f'Lecker, {self.obstauswahl.itemText(idx)}!')
    # end-sample

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HauptFenster()
    window.show()
    sys.exit(app.exec())
