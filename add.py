import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QAbstractItemView, \
    QHeaderView, QWidget
import sqlite3


class Add(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('add.ui', self)