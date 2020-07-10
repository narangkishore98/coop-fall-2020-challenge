class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.stack = [self.value]
        self.other = []

    def add(self, num: int):
  
        self.stack.append(num)
        self.value = sum(self.stack)
   

    def subtract(self, num: int):
        
        self.stack.append(-num)
        self.value = sum(self.stack)
     

    def undo(self):
        if len(self.stack) != 0:

            self.other.append(self.stack.pop())
            self.value = sum(self.stack)
                


    def redo(self):
        if len(self.other) != 0:
            self.stack.append(self.other.pop())
       
            self.value = sum(self.stack)

    def bulk_undo(self, steps: int):
        while steps > 0:
            self.undo()
            steps -= 1

    def bulk_redo(self, steps: int):
        while steps > 0:
            self.redo()
            steps -= 1
