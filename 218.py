from typing import List

class Solution:
    def mergeSkyline(self, left, right):
        res = []
        h1, h2 = 0, 0
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i][0] < right[j][0]:
                x, h1 = left[i]
                i += 1
            elif left[i][0] > right[j][0]:
                x, h2 = right[j]
                j += 1
            else:
                x, h1 = left[i]
                _, h2 = right[j]
                i += 1
                j += 1

            max_height = max(h1, h2)
            if not res or res[-1][1] != max_height:
                res.append([x, max_height])

        res.extend(left[i:])
        res.extend(right[j:])
        
        return res
    
        
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if len(buildings) == 0:
            return []
        if len(buildings) == 1:
            left, right, height = buildings[0]
            return [[left, height], [right, 0]]
        
        mid = len(buildings) // 2
        left_skyline = self.getSkyline(buildings[:mid])
        right_skyline = self.getSkyline(buildings[mid:])
        
        return self.mergeSkyline(left_skyline, right_skyline)
