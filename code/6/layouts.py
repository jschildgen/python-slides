import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFormLayout, QGridLayout, QStackedLayout, QLineEdit, QLabel

buttons = []

class VBox(QWidget):
    # sample(vbox)
    def __init__(self):
        super().__init__()
        self.setWindowTitle('VBox')
        layout = QVBoxLayout()                      # bzw. QHBoxLayout
        layout.addWidget(QPushButton('Eins'))
        layout.addWidget(QPushButton('Zwei'))
        layout.addWidget(QPushButton('Drei'))
        self.setLayout(layout)
    # end-sample

class HBox(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('HBox')
        layout = QHBoxLayout()
        layout.addWidget(QPushButton('Eins'))
        layout.addWidget(QPushButton('Zwei'))
        layout.addWidget(QPushButton('Drei'))
        self.setLayout(layout)

class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Form')
        # sample(form)
        layout = QFormLayout()
        layout.addRow('Name', QLineEdit())
        layout.addRow('Alter', QLineEdit())
        # end-sample
        self.setLayout(layout)

class Grid(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Grid')
        # sample(grid)
        layout = QGridLayout()
        layout.addWidget(QLabel('Eins'), 0, 0)
        layout.addWidget(QLabel('Zwei'), 0, 1)
        layout.addWidget(QLabel('Drei'), 1, 0)
        layout.addWidget(QLabel('Vier'), 1, 1)
        # end-sample
        self.setLayout(layout)

class Stack(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Stacked')
        # sample(stacked)
        layout = QStackedLayout()
        layout.addWidget(QPushButton('Eins'))
        layout.addWidget(QPushButton('Zwei'))
        layout.addWidget(QPushButton('Drei'))
        layout.setCurrentIndex(0)
        # end-sample
        self.keyPressEvent = self.on_key_press

        self.setLayout(layout)

    def on_key_press(self, event):
        if event.key() == 49:   # 49 is the key code for 1
            self.layout().setCurrentIndex(0)
        elif event.key() == 50: # 50 is the key code for 2
            self.layout().setCurrentIndex(1)
        elif event.key() == 51: # 51 is the key code for 3
            self.layout().setCurrentIndex(2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    vbox = VBox()
    vbox.show()
    hbox = HBox()
    hbox.show()
    form = Form()
    form.show()
    grid = Grid()
    grid.show()
    stack = Stack()
    stack.show()
    sys.exit(app.exec())