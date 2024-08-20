class Hello:
    def __init__(self, str):
        self.str = str

class New (Hello):
    def __init__(self, str):
        Hello.__init__(self, str)

    def __str__(self):
        return self.str
