from typing import List


class Solution:
    def distance_squared(self, point):
        return (point[0] - 0) ** 2 + (point[1] - 0) ** 2

    def merge_sort(self, array: List[int], left: int, right: int):
        if left >= right:
            return

        mid = (left + right) // 2
        self.merge_sort(array, left, mid)
        self.merge_sort(array, mid + 1, right)
        self.sort(array, left, mid, right)

    def sort(self, array: List[int], left: int, mid: int, right: int):
        i = left
        j = mid + 1
        temp = []

        while i <= mid and j <= right:
            if array[i] < array[j]:
                temp.append(array[i])
                i += 1
            else:
                temp.append(array[j])
                j += 1

        while i <= mid:
            temp.append(array[i])
            i += 1

        while j <= right:
            temp.append(array[j])
            j += 1

        for k in range(len(temp)):
            array[left + k] = temp[k]

    def partition(self, arr, pivot):
        smaller, equal, larger = [], [], []
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
        return smaller, equal, larger

    def select(self, arr, k):
        if len(arr) <= 5:
            self.merge_sort(arr, 0, len(arr) - 1)
            return arr[k]

        medians = []
        for i in range(0, len(arr), 5):
            group = arr[i : i + 5]
            self.merge_sort(group, 0, len(group) - 1)
            medians.append(group[len(group) // 2])

        pivot = self.select(medians, len(medians) // 2)

        smaller, equal, larger = self.partition(arr, pivot)

        if k < len(smaller):
            return self.select(smaller, k)
        elif k < len(smaller) + len(equal):
            return pivot
        else:
            return self.select(larger, k - len(smaller) - len(equal))

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [self.distance_squared(point) for point in points]

        kth_distance = self.select(distances, k - 1)
        result = []

        for point in points:
            if self.distance_squared(point) <= kth_distance:
                result.append(point)

            if len(result) >= k:
                break

        return result


points = [[2, 1], [4, 2], [1, 3], [2, 4]]

k = 3
result = Solution().kClosest(points, k)
print("K pontos mais próximos da origem:", result)
