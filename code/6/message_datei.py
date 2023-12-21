import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QMessageBox, QFileDialog

class HauptFenster(QWidget):
    def __init__(self):
        super().__init__()
        msg_button = QPushButton('Message')
        msg_button.clicked.connect(self.klick_msg)
        fehler_button = QPushButton('Fehler')
        fehler_button.clicked.connect(self.klick_fehler)
        frage_button = QPushButton('Frage')
        frage_button.clicked.connect(self.klick_frage)
        datei_button = QPushButton('Dateiupload')
        datei_button.setFixedSize(datei_button.sizeHint())
        datei_button.clicked.connect(self.klick_datei)

        layout = QHBoxLayout()
        layout.addWidget(msg_button)
        layout.addWidget(fehler_button)
        layout.addWidget(frage_button)
        layout.addWidget(datei_button)

        self.setLayout(layout)
        self.setWindowTitle('Tolle App')
        self.setFixedSize(400, 100)

    def klick_msg(self):
        # sample(info)
        QMessageBox.information(self, 'Info', 'Dieses Programm ist toll.')
        # end-sample

    def klick_fehler(self):
        # sample(critical)
        QMessageBox.critical(self, 'Fehler', 'Ein Fehler ist aufgetreten.')
        # end-sample

    def klick_frage(self):
        # sample(question)
        antwort = QMessageBox.question(self, 'Beenden', 'Wirklich beenden?')
        if antwort == QMessageBox.StandardButton.Yes:
            self.close()
        # end-sample

    def klick_datei(self):
        # sample(datei)
        datei = QFileDialog.getOpenFileName(self, 'Datei auswählen', 
                                            filter='csv(*.csv)')
        print(datei[0])    # C:/Users/Paula/Desktop/test.csv
        # end-sample

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HauptFenster()
    window.show()
    sys.exit(app.exec())
