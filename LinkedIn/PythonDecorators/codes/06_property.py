"""@property turns a method into a read-only attribute.
Add @<name>.setter to control writes and keep invariants.

Run:  python 06_property.py
"""
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius            # goes through the setter below

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("radius must be positive")
        self._radius = value

    @property
    def area(self):                     # computed, read-only
        return math.pi * self._radius ** 2


if __name__ == "__main__":
    c = Circle(2)
    print("area:", round(c.area, 3))    # read like data: c.area, not c.area()
    c.radius = 3                          # goes through validation
    print("area:", round(c.area, 3))
    try:
        c.radius = -1
    except ValueError as exc:
        print("rejected:", exc)
