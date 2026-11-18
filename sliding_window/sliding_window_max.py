"""
Sliding Window Maximum using a monotonic decreasing deque.
Time: O(n) | Space: O(k)
"""

from collections import deque
from typing import Deque, List


def max_sliding_window(nums: List[int], k: int) -> List[int]:
    if not nums or k <= 0:
        return []

    dq: Deque[int] = deque()
    result: List[int] = []

    for idx, val in enumerate(nums):
        while dq and dq[0] <= idx - k:
            dq.popleft()
        while dq and nums[dq[-1]] <= val:
            dq.pop()
        dq.append(idx)
        if idx >= k - 1:
            result.append(nums[dq[0]])

    return result
