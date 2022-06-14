from typing import List


# from math import abs


class Singleton(object):
    sticks: List[int] = []

    _x = 0

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

    def solve(self, sticks: List[int]) -> int:
        # clear field _x
        self._x = 0
        self.sticks = sticks

        if (
            self.sticks is None or len(self.sticks) == 1
        ):  # if we have only one or no elem result will be 0
            return self._x

        avg_len = sum(self.sticks) // len(self.sticks)

        for i in range(len(self.sticks)):
            if self.sticks[i] == avg_len:
                continue
            self._x += abs(self.sticks[i] - avg_len)
        return self._x
