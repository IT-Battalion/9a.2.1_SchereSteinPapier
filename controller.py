import random

from model import SchereSteinPapier
from view import View


class Controller:
    def __init__(self):
        self.model = SchereSteinPapier()
        self.view = View(self)
        self.view.show()

    def execute(self):
        p = self.view.get_player()
        c = random.randint(0, 2)
        self.view.set_results(p, c)
        error = self.model.execute(p, c)
        if error > -1:
            self.view.increase_round_counter()
            if error == 0:
                self.view.increase_player_score()
                self.view.set_text_statusbar("Du hast gewonnen!")
                self.view.set_text_statusbar("Wähle deinen nächsten Zug!")
            elif error == 1:
                self.view.increase_computer_score()
                self.view.set_text_statusbar("Du hast verloren!")
                self.view.set_text_statusbar("Wähle deinen nächsten Zug!")
            else:
                self.view.set_text_statusbar("Unentschieden!")
                self.view.set_text_statusbar("Wähle deinen nächsten Zug!")
        else:
            self.view.set_text_statusbar(error)

    def reset(self):
        self.view.reset()
        self.model.reset()
