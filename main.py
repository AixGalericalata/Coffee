import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QAbstractItemView, \
    QHeaderView
import sqlite3


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        con = sqlite3.connect('coffee.sqlite')

        cur = con.cursor()

        result = cur.execute("""SELECT * FROM coffee""").fetchall()

        roast = ['Сырые зёрна', 'Светлая', 'Средняя', 'Тёмная', 'Высшая']
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(7)
        for i, elem in enumerate(result):
            item0 = QTableWidgetItem(str(elem[0]))
            item1 = QTableWidgetItem(elem[1])
            item2 = QTableWidgetItem(roast[elem[2]])
            item3 = QTableWidgetItem('Молотый' if elem[3] == 'True' else 'Зерновой')
            item4 = QTableWidgetItem(elem[4])
            item5 = QTableWidgetItem(str(elem[5]))
            item6 = QTableWidgetItem(str(elem[6]))
            self.tableWidget.setItem(i, 0, item0)
            self.tableWidget.setItem(i, 1, item1)
            self.tableWidget.setItem(i, 2, item2)
            self.tableWidget.setItem(i, 3, item3)
            self.tableWidget.setItem(i, 4, item4)
            self.tableWidget.setItem(i, 5, item5)
            self.tableWidget.setItem(i, 6, item6)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.tableWidget.setHorizontalHeaderLabels(
            ['Номер', 'Название сорта', 'Степень прожарки', 'Помол', 'Описание', 'Цена', 'Объем'])
        self.tableWidget.verticalHeader().hide()
        #  self.table.itemSelectionChanged.connect(self.selected)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.resizeColumnsToContents()

        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
