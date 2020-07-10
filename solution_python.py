class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.stack = []
        self.track = -1

    def add(self, num: int):
        self.value += num
        self.stack.append(self.value)
        self.track += 1

    def subtract(self, num: int):
        self.value -= num
        self.append(self.value)
        self.track += 1

    def undo(self):
        #self.track -= 1
        if track == 0:
            self.value = self.stack[self.track]
        else:
            self.track -= 1
            self.value = self.stack[self.track]


    def redo(self):
        if self.track<len(self.stack)-1:
            self.track+=1
            self.value=self.stack[self.track]

    def bulk_undo(self, steps: int):
        pass

    def bulk_redo(self, steps: int):
        pass
