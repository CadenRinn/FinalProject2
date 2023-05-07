from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import random

class Ui_MainWindow(object):

    def setupUi(self, MainWindow) -> None:
        """
        Creates the Window for the Game Board
        :param MainWindow: Window from Qt Designer
        :return: None
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setMinimumSize(QtCore.QSize(800, 800))
        MainWindow.setMaximumSize(QtCore.QSize(800, 800))
        MainWindow.setStyleSheet("background-color: rgb(115, 115, 115);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TTT_label = QtWidgets.QLabel(self.centralwidget)
        self.TTT_label.setGeometry(QtCore.QRect(200, -10, 411, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.TTT_label.setFont(font)
        self.TTT_label.setObjectName("TTT_label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(160, 130, 466, 471))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gameboard = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gameboard.setContentsMargins(0, 0, 0, 0)
        self.gameboard.setObjectName("gameboard")
        self.B2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.B2.setMinimumSize(QtCore.QSize(150, 150))
        self.B2.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.B2.setFont(font)
        self.B2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.B2.setText("")
        self.B2.setObjectName("B2")
        self.gameboard.addWidget(self.B2, 1, 1, 1, 1)
        self.A3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.A3.setMinimumSize(QtCore.QSize(150, 150))
        self.A3.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.A3.setFont(font)
        self.A3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.A3.setText("")
        self.A3.setObjectName("A3")
        self.gameboard.addWidget(self.A3, 0, 2, 1, 1)
        self.C3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.C3.setMinimumSize(QtCore.QSize(150, 150))
        self.C3.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.C3.setFont(font)
        self.C3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.C3.setText("")
        self.C3.setObjectName("C3")
        self.gameboard.addWidget(self.C3, 2, 2, 1, 1)
        self.B1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.B1.setMinimumSize(QtCore.QSize(150, 150))
        self.B1.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.B1.setFont(font)
        self.B1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.B1.setText("")
        self.B1.setObjectName("B1")
        self.gameboard.addWidget(self.B1, 1, 0, 1, 1)
        self.A2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.A2.setMinimumSize(QtCore.QSize(150, 150))
        self.A2.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.A2.setFont(font)
        self.A2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.A2.setText("")
        self.A2.setObjectName("A2")
        self.gameboard.addWidget(self.A2, 0, 1, 1, 1)
        self.A1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.A1.setMinimumSize(QtCore.QSize(150, 150))
        self.A1.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.A1.setFont(font)
        self.A1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.A1.setText("")
        self.A1.setObjectName("A1")
        self.gameboard.addWidget(self.A1, 0, 0, 1, 1)
        self.C2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.C2.setMinimumSize(QtCore.QSize(150, 150))
        self.C2.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.C2.setFont(font)
        self.C2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.C2.setText("")
        self.C2.setObjectName("C2")
        self.gameboard.addWidget(self.C2, 2, 1, 1, 1)
        self.B3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.B3.setMinimumSize(QtCore.QSize(150, 150))
        self.B3.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.B3.setFont(font)
        self.B3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.B3.setText("")
        self.B3.setObjectName("B3")
        self.gameboard.addWidget(self.B3, 1, 2, 1, 1)
        self.C1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.C1.setMinimumSize(QtCore.QSize(150, 150))
        self.C1.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.C1.setFont(font)
        self.C1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.C1.setText("")
        self.C1.setObjectName("C1")
        self.gameboard.addWidget(self.C1, 2, 0, 1, 1)
        self.user_label = QtWidgets.QLabel(self.centralwidget)
        self.user_label.setGeometry(QtCore.QRect(50, 660, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.user_label.setFont(font)
        self.user_label.setObjectName("user_label")
        self.computer_label = QtWidgets.QLabel(self.centralwidget)
        self.computer_label.setGeometry(QtCore.QRect(430, 660, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.computer_label.setFont(font)
        self.computer_label.setObjectName("computer_label")
        self.userscore_label = QtWidgets.QLabel(self.centralwidget)
        self.userscore_label.setGeometry(QtCore.QRect(190, 670, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.userscore_label.setFont(font)
        self.userscore_label.setObjectName("userscore_label")
        self.computerscore_label = QtWidgets.QLabel(self.centralwidget)
        self.computerscore_label.setGeometry(QtCore.QRect(630, 660, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.computerscore_label.setFont(font)
        self.computerscore_label.setObjectName("computerscore_label")
        self.game_button = QtWidgets.QPushButton(self.centralwidget)
        self.game_button.setGeometry(QtCore.QRect(200, 610, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.game_button.setFont(font)
        self.game_button.setStyleSheet("background-color: rgb(218, 208, 200);")
        self.game_button.setObjectName("game_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 90, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.score_button = QtWidgets.QPushButton(self.centralwidget)
        self.score_button.setGeometry(QtCore.QRect(410, 610, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.score_button.setFont(font)
        self.score_button.setStyleSheet("background-color: rgb(218, 208, 200);")
        self.score_button.setObjectName("score_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow) -> None:
        """
        Method to set the text and titles of widgets
        :param MainWindow: Main Window from Qt Designer
        :return: None
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TTT_label.setText(_translate("MainWindow", "Tic-Tac-Toe Game"))
        self.user_label.setText(_translate("MainWindow", "Your Score: "))
        self.computer_label.setText(_translate("MainWindow", "Computer Score: "))
        self.userscore_label.setText(_translate("MainWindow", "0"))
        self.computerscore_label.setText(_translate("MainWindow", "0"))
        self.game_button.setText(_translate("MainWindow", "New Game"))
        self.score_button.setText(_translate("MainWindow", "Reset Score"))

    def clicker(self, b) -> None:
        """
        Receives player input and computer input
        :param b: Receives click input from Qt Designer
        :return: Does not return data: modifies label of buttons
        """
        b.setText('X')
        b.setEnabled(False)
        # Checks is user input led to a win
        self.checkWin()
        # Case for if computer goes (Last player choice fills the board so computer can't go)
        button_list = [
            self.A1,
            self.A2,
            self.A3,
            self.B1,
            self.B2,
            self.B3,
            self.C1,
            self.C2,
            self.C3]
        x = 0
        for a in button_list:
            if a.text() != '':
                x += 1
        if x<8 and self.label.text()=='':
            self.computer()
            self.checkWin()


    def reset(self) -> None:
        """
        Resets game board
        :return: None
        """
        button_list = [
            self.A1,
            self.A2,
            self.A3,
            self.B1,
            self.B2,
            self.B3,
            self.C1,
            self.C2,
            self.C3]

        for b in button_list:
            b.setText('')
            b.setEnabled(True)
            b.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText('')



    def score_reset(self) -> None:
        """
        Resets User and Computer Scores
        :return: None: Modifies userscore and computerscore variables
        """
        self.userscore_label.setText('0')
        self.computerscore_label.setText('0')

    def computer(self):
        """
        Randomly Selects Computer's Move
        :return: None: Modifies selected square
        """
        option = random.randint(1, 9)
        x = 0
        # While the option is taken, option is randomized until an open square works
        while x == 0:
            if option == 1 and self.A1.text() == '':
                self.A1.setText('O')
                self.A1.setEnabled(False)
                x+=1
            elif option == 2 and self.A2.text() == '':
                self.A2.setText('O')
                self.A2.setEnabled(False)
                x+=1
            elif option == 3 and self.A3.text() == '':
                self.A3.setText('O')
                self.A3.setEnabled(False)
                x+=1
            elif option == 4 and self.B1.text() == '':
                self.B1.setText('O')
                self.B1.setEnabled(False)
                x+=1
            elif option == 5 and self.B2.text() == '':
                self.B2.setText('O')
                self.B2.setEnabled(False)
                x+=1
            elif option == 6 and self.B3.text() == '':
                self.B3.setText('O')
                self.B3.setEnabled(False)
                x+=1
            elif option == 7 and self.C1.text() == '':
                self.C1.setText('O')
                self.C1.setEnabled(False)
                x+=1
            elif option == 8 and self.C2.text() == '':
                self.C2.setText('O')
                self.C2.setEnabled(False)
                x+=1
            elif option == 9 and self.C3.text() == '':
                self.C3.setText('O')
                self.C3.setEnabled(False)
                x+=1
            else:
                option = random.randint(1, 9)


    def checkWin(self) -> None:
        """
        Has win conditions for Tic-tac-toe
        :return: Send winning squares to win() or tiegame()
        """
        ##Checks top row
        if self.A1.text() != "" and self.A1.text() == self.A2.text() and self.A1.text() == self.A3.text():
            self.win(self.A1, self.A2, self.A3)
        ##Checks middle row
        if self.B1.text() != "" and self.B1.text() == self.B2.text() and self.B1.text() == self.B3.text():
            self.win(self.B1, self.B2, self.B3)
        ##Checks bottom row
        if self.C1.text() != "" and self.C1.text() == self.C2.text() and self.C1.text() == self.C3.text():
            self.win(self.C1, self.C2, self.C3)
        ##Checks left column
        if self.A1.text() != "" and self.A1.text() == self.B1.text() and self.A1.text() == self.C1.text():
            self.win(self.A1, self.B1, self.C1)
        ##Checks middle column
        if self.A2.text() != "" and self.A2.text() == self.B2.text() and self.A2.text() == self.C2.text():
            self.win(self.A2, self.B2, self.C2)
        ##Checks right column
        if self.A3.text() != "" and self.A3.text() == self.B3.text() and self.A3.text() == self.C3.text():
            self.win(self.A3, self.B3, self.C3)
        ##Checks diagonally from top left to bottom right
        if self.A1.text() != "" and self.A1.text() == self.B2.text() and self.A1.text() == self.C3.text():
            self.win(self.A1, self.B2, self.C3)
        ##Checks diagonally from top right to bottom left
        if self.C1.text() != "" and self.C1.text() == self.B2.text() and self.C1.text() == self.A3.text():
            self.win(self.A3, self.B2, self.C1)
        ##Otherwise it is a tie
        elif self.A1.text() != "" and self.A2.text() != "" and self.A3.text() != "" and self.B1.text() != "" and self.B2.text() != "" and self.B3.text() != "" and self.C1.text() != "" and self.C2.text() != "" and self.C3.text() != "" and self.label.text() == '':
            self.tiegame()


    def win(self, a, b, c) -> None:
        """
        Disables game board, informs user of whom won
        :param a: First square from win condition
        :param b: Second square from win condition
        :param c: Third square from win condition
        :return: None: Modifies score and label variables
        """


        a.setStyleSheet('QPushButton {color: green;}')
        b.setStyleSheet('QPushButton {color: green;}')
        c.setStyleSheet('QPushButton {color: green;}')
        self.disable()
        # Case for if player wins
        if a.text() == 'X':
            self.label.setText('You Won!')
            num = int(self.userscore_label.text())
            num +=1
            self.userscore_label.setText(str(num))
            # Case if the computer wins
        if a.text() == 'O':
            self.label.setText('Computer Won!')
            num = int(self.computerscore_label.text())
            num +=1
            self.computerscore_label.setText(str(num))
        button_list = [
            self.A1,
            self.A2,
            self.A3,
            self.B1,
            self.B2,
            self.B3,
            self.C1,
            self.C2,
            self.C3]

        for button in button_list:
            button.setStyleSheet("background-color: rgb(0, 0, 0);")

    def tiegame(self) -> None:
        """
        Disables game board and notifies of tie game
        :return: None: Modifies label
        """
        self.label.setText("It's a draw.")
        self.disable()
        button_list = [
            self.A1,
            self.A2,
            self.A3,
            self.B1,
            self.B2,
            self.B3,
            self.C1,
            self.C2,
            self.C3]

        for b in button_list:
            b.setStyleSheet("background-color: rgb(0, 0, 0);")

    def disable(self) -> None:
        """
        Disabled game board after a win
        :return:None
        """
        button_list = [
            self.A1,
            self.A2,
            self.A3,
            self.B1,
            self.B2,
            self.B3,
            self.C1,
            self.C2,
            self.C3]

        for b in button_list:
            b.setEnabled(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())