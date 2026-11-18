"""
Running Median of a Real-Time Data Stream using balanced max-heap and min-heap.
Time: O(log n) add(), O(1) median() | Space: O(n)
"""

import heapq
from typing import List


class MedianStream:
    def __init__(self) -> None:
        self._low: List[int] = []   # max-heap via negated values
        self._high: List[int] = []  # min-heap

    def add(self, num: int) -> None:
        heapq.heappush(self._low, -num)
        heapq.heappush(self._high, -heapq.heappop(self._low))
        if len(self._high) > len(self._low):
            heapq.heappush(self._low, -heapq.heappop(self._high))

    def median(self) -> float:
        if not self._low:
            raise ValueError("stream is empty")
        if len(self._low) > len(self._high):
            return float(-self._low[0])
        return (-self._low[0] + self._high[0]) / 2.0
