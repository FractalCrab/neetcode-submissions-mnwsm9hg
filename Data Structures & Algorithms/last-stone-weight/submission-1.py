def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


import heapq as hq

class Solution:
    def lastStoneWeight(self, stones):
        
        heap = stones[:] 
        heapq.heapify_max(heap)           
        
        while len(heap) > 1:
            y = hq.heappop_max(heap)
            x = hq.heappop_max(heap)

            if x != y:
                hq.heappush_max(heap, (y - x))
        
        return heap[0] if heap else 0
                
