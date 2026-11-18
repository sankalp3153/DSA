"""
Subarray Sum Equals K using prefix-sum frequency hash map.
Time: O(n) | Space: O(n)
"""

from collections import defaultdict
from typing import List


def subarray_sum(nums: List[int], k: int) -> int:
    prefix_counts: dict[int, int] = defaultdict(int)
    prefix_counts[0] = 1
    running = 0
    total = 0

    for num in nums:
        running += num
        total += prefix_counts[running - k]
        prefix_counts[running] += 1

    return total
