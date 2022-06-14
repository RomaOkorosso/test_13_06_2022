from typing import List
from math import ceil


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

        self.sticks.sort()
        right_middle = ceil(len(self.sticks) / 2)
        left_middle = len(self.sticks) // 2

        self._x = sum(sticks[right_middle:]) - sum(sticks[:left_middle])
        # get sum of right(from middle) values of arr and left, that will be our answer

        return self._x
