import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtGui import QPainter, QColor
import random
import sqlite3


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        con = sqlite3.connect('coffee.sqlite')

        cur = con.cursor()

        result = cur.execute("""SELECT * FROM coffee""").fetchall()

        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(7)
        for i, elem in enumerate(result):
            item0 = QTableWidgetItem(str(elem[0]))
            item1 = QTableWidgetItem(str(elem[1]))
            item2 = QTableWidgetItem(str(elem[2]))
            item3 = QTableWidgetItem(str(elem[3]))
            item4 = QTableWidgetItem(str(elem[4]))
            item5 = QTableWidgetItem(str(elem[5]))
            item6 = QTableWidgetItem(str(elem[6]))
            self.tableWidget.setItem(i, 0, item0)
            self.tableWidget.setItem(i, 1, item1)
            self.tableWidget.setItem(i, 2, item2)
            self.tableWidget.setItem(i, 3, item3)
            self.tableWidget.setItem(i, 4, item4)
            self.tableWidget.setItem(i, 5, item5)
            self.tableWidget.setItem(i, 6, item6)


        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
