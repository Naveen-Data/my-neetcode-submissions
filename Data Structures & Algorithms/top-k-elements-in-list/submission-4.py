import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: frequency map
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Step 2: min-heap to keep top k
        heap = []

        for num, count in freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, num))
            else:
                # heap[0] is the weakest (smallest frequency)
                if count > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (count, num))

        # Step 3: extract elements
        return [num for count, num in heap]