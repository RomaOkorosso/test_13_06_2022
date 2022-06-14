import pytest
from oop import Singleton


def test_singleton_cannot_be_instantiated_twice():
    s = Singleton()
    s1 = Singleton()
    assert s == s1


def test_singleton_is_singleton():
    s = Singleton()
    s.sticks, s._x = [], 0
    s.sticks = [1, 2, 3]
    s1 = Singleton()
    s_sticks, s1_sticks = s.sticks, s1.sticks
    del s, s1
    assert s_sticks == s1_sticks


def test_one_stick():
    s = Singleton()
    sticks = [1]
    assert s.solve(sticks) == 0


def test_same_sticks():
    s = Singleton()
    sticks = [1, 1]
    assert s.solve(sticks) == 0


def test_different_sticks():
    s = Singleton()
    sticks = [1, 2, 4, 5]
    assert s.solve(sticks) == 6


def test_multiple_sticks():
    s = Singleton()
    sticks = [1, 2, 4, 5, 5, 4, 3, 2, 1]
    assert s.solve(sticks) == 12


def test_simple():
    s = Singleton()
    sticks = [159, 201, 307, 377]
    assert s.solve(sticks) == 324


def test_medium():
    sticks = [
        89102,
        67640,
        35846,
        75062,
        16095,
        78102,
        122829,
        121590,
        139143,
        116606,
        163595,
        64502,
        150437,
        128450,
        89519,
        15018,
        55031,
        100636,
        123211,
        77092,
        108579,
        9044,
        156971,
        85092,
        45169,
        166688,
        140259,
        45890,
        111747,
        144264,
        104525,
        175476,
        173719,
        49844,
        46267,
        129262,
        8169,
        30000,
        35537,
        85304,
        84475,
        96186,
        154807,
        182570,
        155055,
        50050,
        129099,
        151216,
        160293,
        185802,
        26847,
        102586,
        10397,
        175608,
        16593,
        178530,
        135531,
        94814,
        194599,
        61298,
        60253,
        172020,
        187227,
        174746,
        163363,
        62316,
        62991,
        141822,
        31921,
        25816,
        68373,
        192366,
        2529,
        185250,
        92557,
        39646,
        94131,
        163388,
        186901,
        199614,
        71833,
        122342,
        26837,
        162908,
        15877,
        93896,
        93267,
        61060,
        140947,
        139314,
        54239,
        75500,
        79481,
        100222,
        169733,
        196360,
        194907,
        65588,
        148523,
        120968,
    ]
    s = Singleton()
    assert s.solve(sticks) == 4836692


def test_hard():
    with open("hard_test_coords.txt", "r") as f:
        sticks = f.readlines()
        sticks = list(map(int, *[l.split(" ") for l in sticks]))

    s = Singleton()

    assert s.solve(sticks) == 5233919113
