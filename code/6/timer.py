import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox
from PyQt6.QtCore import QTimer

class HauptFenster(QWidget):
    def __init__(self):
        super().__init__()
        # sample(timer)
        self.seconds = 0
        self.timer = QTimer(self)
        self.timer.start(1000)     # alle 1000 ms
        self.timer.timeout.connect(self.on_timer)
        # end-sample

        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        self.setLayout(layout)
        
        self.setWindowTitle('Stoppuhr')
        self.setFixedSize(200, 100)

    # sample(on_timer)
    def on_timer(self):
        self.seconds += 1
        m = self.seconds // 60 # Ganzzahldivision
        s = self.seconds % 60  # Rest (Modulo)
        if s < 10:
            s = f'0{s}'
        self.label.setText(f'{m}:{s}')
    # end-sample

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HauptFenster()
    window.show()
    sys.exit(app.exec())
