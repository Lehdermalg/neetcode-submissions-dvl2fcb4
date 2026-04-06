class MinStack:

    def __init__(self):
        # we save data as a 3-tuple: 'current, min, max'
        self.s = []

    def push(self, val: int) -> None:
        if len(self.s) == 0:
            last = (val, val, val)
        else:
            last = self._top

        _min = min(last[1], val)
        _max = max(last[2], val)
        self.s.append((val, _min, _max))

    def pop(self) -> None:
        self.s.pop()

    @property
    def _top(self) -> tuple:
        return self.s[-1]

    def _val(self, t: tuple) -> int:
        return t[0]

    def _min(self, t: tuple) -> int:
        return t[1]

    def _max(self, t: tuple) -> int:
        return t[2]

    def top(self) -> int:
        print(f"top: {self.s}")
        return self._val(self._top)

    def getMin(self) -> int:
        return self._min(self._top)
