import sys
from random import randint

import self
from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QApplication
from layout import *

class MyForm(QDialog):

    def reserwacja(self):
        if self.ui.radioButton.isChecked():
            specjalizacja = 'Internista'
        elif self.ui.radioButton_2.isChecked():
            specjalizacja = 'Pediatra'
        else:
            specjalizacja = 'Dermatolog'

        if self.ui.checkBox.isChecked():
            dni = randint(0, 14)
            cena = 200

        else:
            dni = randint(0, 1000)
            cena = 0

        self.ui.label_text.setText(
            f"Pomyślnie zarezerwowano wizytę u lekarza: {specjalizacja}. Termin wizyty przypada za: {dni}. Koszt wizyty: {cena}."
        )

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.Reserv.clicked.connect(self.reserwacja)
        self.show()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec())


