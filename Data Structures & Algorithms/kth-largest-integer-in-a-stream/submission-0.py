import heapq as hq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        self.nums.append(val)
        return self.kth_largest()

    def kth_largest(self) -> int:
        min_heap = []

        for val in self.nums:
            hq.heappush(min_heap, val)

            if len(min_heap) > self.k:
                hq.heappop(min_heap)
        return min_heap[0]