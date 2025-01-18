import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PyQt6 import uic
from pathlib import Path


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi(Path('main.ui'), self)
        self.name_db = 'coffee.sqlite'
        self.setFixedSize(500, 500)
        res = sqlite3.connect(self.name_db).cursor().execute('SELECT coffee.id, coffee.name, coffee.degree, types.type, coffee.description, coffee.price, coffee.volume FROM coffee INNER JOIN types ON types.id = coffee.type;').fetchall()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        self.paste_data(res)

    def paste_data(self, res):
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
