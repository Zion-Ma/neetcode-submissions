class CountSquares:

    def __init__(self):
        self.points: dict[tuple, int] = dict()

    def add(self, point: List[int]) -> None:
        if (point[0], point[1]) not in self.points:
            self.points[(point[0], point[1])] = 0
        self.points[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        qx, qy = point
        count = 0
        for x, y in self.points:
            if (x == qx) or (y == qy) or abs(qx - x) != abs(qy - y):
                continue
            if (qx, y) in self.points and (x, qy) in self.points:
                count += self.points[(x, y)] * self.points[(qx, y)] * self.points[(x, qy)]
        return count
