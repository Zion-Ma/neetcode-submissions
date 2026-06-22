class CountSquares:

    def __init__(self):
        self.points: dict[tuple, int] = dict()

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] = 1 + self.points.get((x, y), 0)
    
    def isDiagnal(self, point1: List[int], point2: tuple) -> bool:
        return abs(point1[0] - point2[0]) == abs(point1[1] - point2[1])
    
    def isSelf(self, point1: List[int], point2: tuple) -> bool:
        return point1[0] == point2[0] and point1[1] == point2[1]

    def count(self, point: List[int]) -> int:
        # print("=========")
        # print(point)
        res = 0
        for p in self.points:
            if not self.isDiagnal(point, p) or self.isSelf(point, p):
                continue
            diag_count = self.points[p]
            vertical_count = self.points.get((p[0], point[1]), 0)
            horizontal_count = self.points.get((point[0], p[1]), 0)
            # print(f"diag: {diag_count}")
            # print(f"vertical_count: {vertical_count}")
            # print(f"horizontal_count: {horizontal_count}")
            res += diag_count * vertical_count * horizontal_count
            # if res != 0:
            #     print(p)
        return res
