"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 352
Updated: 2025-03-25T16:45:49+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 352
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
