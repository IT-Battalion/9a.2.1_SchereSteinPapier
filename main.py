import sys

from PyQt6.QtWidgets import QApplication

from controller import Controller
from model import SchereSteinPapier

qt = QApplication([])
m = SchereSteinPapier()
c = Controller()
sys.exit(qt.exec())
