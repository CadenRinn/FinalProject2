from PyQt5.QtWidgets import *
from Tictactoe import *


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setupUi(self)
        self.A1.clicked.connect(lambda: self.clicker(self.A1))
        self.A2.clicked.connect(lambda: self.clicker(self.A2))
        self.A3.clicked.connect(lambda: self.clicker(self.A3))
        self.B1.clicked.connect(lambda: self.clicker(self.B1))
        self.B2.clicked.connect(lambda: self.clicker(self.B2))
        self.B3.clicked.connect(lambda: self.clicker(self.B3))
        self.C1.clicked.connect(lambda: self.clicker(self.C1))
        self.C2.clicked.connect(lambda: self.clicker(self.C2))
        self.C3.clicked.connect(lambda: self.clicker(self.C3))
        self.game_button.clicked.connect(lambda: self.reset())
        self.score_button.clicked.connect(lambda: self.score_reset())

