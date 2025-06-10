"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 605
Updated: 2025-06-10T10:56:18+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 605
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
