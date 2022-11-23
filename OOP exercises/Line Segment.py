from __future__ import annotations

import math


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class LineSegment:
    def __init__(self, p: Point, q: Point):
        self.p = p
        self.q = q

    def slope(self):
        return (self.p.y - self.q.y) / (self.p.x - self.q.x)

    def length(self):
        return math.sqrt((self.q.x- self.p.x)**2 + (self.q.y - self.p.y)**2)



segment = LineSegment(Point(1, 1), Point(3, 2))
print(segment.slope())
print(segment.length())
