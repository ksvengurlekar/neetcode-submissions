class MinStack:

    def __init__(self):
        self.order = deque()
        self.mono = deque()
        

    def push(self, val: int) -> None:
        self.order.append(val)
        if not self.mono or val <= self.mono[-1]:
            self.mono.append(val)
        

    def pop(self) -> None:
        if self.order[-1] == self.mono[-1]:
            self.mono.pop()

        self.order.pop()
        

    def top(self) -> int:
        return self.order[-1]
        

    def getMin(self) -> int:
        return self.mono[-1]


