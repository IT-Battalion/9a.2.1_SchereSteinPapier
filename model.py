class SchereSteinPapier:
    def __init__(self):
        self.p = None
        self.c = None
        self.result = None
        self.error = None

    def reset(self):
        self.p = None
        self.c = None
        self.result = None
        self.error = None

    # 0 = player
    # 1 = computer
    # 3 = unentschieden
    # -1 = error
    def execute(self, p: int, c: int):
        self.p = p
        self.c = c

        # 0 = Schere
        # 1 = Stein
        # 2 = Papier
        if self.p == self.c:
            self.result = 3
            return self.result
        elif self.p == 0:
            if self.c == 1:
                self.result = 1
            elif self.c == 2:
                self.result = 0
            return self.result
        elif self.p == 1:
            if self.c == 0:
                self.result = 0
            elif self.c == 2:
                self.result = 1
            return self.result
        elif self.p == 2:
            if self.c == 0:
                self.result = 1
            elif self.c == 1:
                self.result = 0
            return self.result
        else:
            self.error = "Error calculation the winner!"
            self.result = -1
            return self.result

