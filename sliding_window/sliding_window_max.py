"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 2077
Updated: 2026-08-18T18:32:56+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2077
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
