import sys
from PyQt5.QtWidgets import QApplication, QWidget

class HauptFenster(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tolle Anwendung')
        self.setFixedSize(300, 100)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HauptFenster()
    window.show()
    sys.exit(app.exec_())