from PyQt6 import uic
from PyQt6.QtWidgets import *


class View(QMainWindow):
    pb_execute: QPushButton
    pb_reset: QPushButton
    pb_reset: QPushButton
    player_score: QLabel
    computer_score: QLabel
    round_counter: QLabel
    tool_select: QComboBox
    statusbar: QStatusBar
    result_computer: QLabel
    result_player: QLabel

    stone = "🪨"
    scissors = "✂️"
    paper = "🕮"

    def __init__(self, c):
        super().__init__()
        uic.loadUi("GUI.ui", self)
        self.tool_select.addItem("Schere")
        self.tool_select.addItem("Stein")
        self.tool_select.addItem("Papier")
        self.pb_execute.clicked.connect(c.execute)
        self.pb_reset.clicked.connect(c.reset)
        self.set_text_statusbar("Wähle deinen nächsten Zug!")

    def reset(self) -> None:
        self.tool_select.setCurrentIndex(0)
        self.round_counter.setText("0")
        self.computer_score.setText("0")
        self.player_score.setText("0")
        self.set_results("Noch keine Runde!", "Noch keine Runde!")
        self.set_text_statusbar("Wähle deinen nächsten Zug!")

    def increase_round_counter(self) -> None:
        self.round_counter.setText(str(int(self.round_counter.text()) + 1))

    def increase_player_score(self) -> None:
        self.player_score.setText(str(int(self.player_score.text()) + 1))

    def increase_computer_score(self) -> None:
        self.computer_score.setText(str(int(self.computer_score.text()) + 1))

    # 0 = Schere
    # 1 = Stein
    # 2 = Papier
    def get_player(self):
        return self.tool_select.currentIndex()

    def set_text_statusbar(self, msg: str):
        self.statusbar.showMessage(msg)

    def convert_text_to_icon(self, text):
        if text == 0:
            return self.scissors
        elif text == 1:
            return self.stone
        elif text == 2:
            return self.paper
        else:
            return "Error"

    def set_results(self, p: str, c: str):
        c_text = self.convert_text_to_icon(c)
        p_text = self.convert_text_to_icon(p)
        self.result_player.setText(p_text)
        self.result_computer.setText(c_text)
