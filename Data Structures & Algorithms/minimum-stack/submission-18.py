class MinStack:

    def __init__(self):
        # we save data as a 3-tuple: 'current, min, max'
        self.s = []

    def push(self, val: int) -> None:
        if not self.s :
            last = (val, val, val)
        else:
            last = self.s[-1]

        _min = min(last[1], val)
        _max = max(last[2], val)
        self.s.append((val, _min, _max))

    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        print(f"top: {self.s}")
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.s[-1][1]
