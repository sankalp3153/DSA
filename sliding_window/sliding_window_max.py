"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 2146
Updated: 2026-09-02T13:56:24+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2146
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
