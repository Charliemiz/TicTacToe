from PyQt5.QtWidgets import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        # Create a list of all the buttons in order to iterate many times later
        self.button_list = [
            self.Button_1,
            self.Button_2,
            self.Button_3,
            self.Button_4,
            self.Button_5,
            self.Button_6,
            self.Button_7,
            self.Button_8,
            self.Button_9
        ]

        self.label.setVisible(False)
        self.Button_Start.setEnabled(True)
        self.Button_Restart.setEnabled(False)
        for button in self.button_list:
            button.setDisabled(True)

        # starting turns at 0, so it begins with X then O ...
        self.turns = 0

        # Define a counter to keep track of whose turn it is
        self.counter = 0

        # connecting the buttons to the clicker function
        self.Button_1.clicked.connect(lambda: self.clicker(self.Button_1))
        self.Button_2.clicked.connect(lambda: self.clicker(self.Button_2))
        self.Button_3.clicked.connect(lambda: self.clicker(self.Button_3))
        self.Button_4.clicked.connect(lambda: self.clicker(self.Button_4))
        self.Button_5.clicked.connect(lambda: self.clicker(self.Button_5))
        self.Button_6.clicked.connect(lambda: self.clicker(self.Button_6))
        self.Button_7.clicked.connect(lambda: self.clicker(self.Button_7))
        self.Button_8.clicked.connect(lambda: self.clicker(self.Button_8))
        self.Button_9.clicked.connect(lambda: self.clicker(self.Button_9))

        self.Button_Restart.clicked.connect(lambda: self.restart())
        self.Button_Start.clicked.connect(lambda: self.start())

    def checkWin(self):
        # Create a list of all the winning combinations
        winning_combinations = [
            [self.Button_1, self.Button_2, self.Button_3],
            [self.Button_4, self.Button_5, self.Button_6],
            [self.Button_7, self.Button_8, self.Button_9],
            [self.Button_1, self.Button_4, self.Button_7],
            [self.Button_2, self.Button_5, self.Button_8],
            [self.Button_3, self.Button_6, self.Button_9],
            [self.Button_1, self.Button_5, self.Button_9],
            [self.Button_3, self.Button_5, self.Button_7]
        ]

        # Check all the winning combinations to see if there is a winner
        for combination in winning_combinations:
            if combination[0].text() == combination[1].text() == combination[2].text() != "":
                self.win(combination[0], combination[1], combination[2])
                return
                # Exits function if winner is found

        # Check if all buttons have been clicked
        clicked_buttons = [self.Button_1, self.Button_2, self.Button_3, self.Button_4, self.Button_5, self.Button_6,
                           self.Button_7, self.Button_8, self.Button_9]
        for button in clicked_buttons:
            if button.text() == "":
                return
                # Exits function if all buttons are clicked with no winner found

        self.label.setText(f"Game Over, It's a Tie!")

    def win(self, a, b, c):
        # Disable all the buttons so the game can't continue
        for button in [self.Button_1, self.Button_2, self.Button_3, self.Button_4, self.Button_5, self.Button_6,
                       self.Button_7, self.Button_8, self.Button_9]:
            button.setEnabled(False)

        # Highlight the winning combination of buttons
        a.setStyleSheet("background-color: green")
        b.setStyleSheet("background-color: green")
        c.setStyleSheet("background-color: green")

        # Display the winning message
        winner = a.text()
        self.label.setText(f"{winner} wins!")

    # Click the buttons
    def clicker(self, button):
        if self.counter % 2 == 0:
            mark = "X"
            self.label.setText("O's Turn")
        else:
            mark = "O"
            self.label.setText("X's Turn")

        button.setText(mark)
        button.setEnabled(False)

        # Increment the counter
        self.counter += 1

        self.checkWin()

    # Begin Game
    def start(self):
        self.Button_Restart.setEnabled(True)
        for button in self.button_list:
            button.setEnabled(True)
        self.Button_Start.setDisabled(True)
        self.label.setVisible(True)

    # Start Over
    def restart(self):
        # Reset the buttons text and color
        for b in self.button_list:
            b.setText("")
            b.setEnabled(True)
            b.setStyleSheet("background-color: #default")

        # Reset the label
        self.label.setText("X Goes First!")

        # Reset counter
        self.counter = 0
