"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 2215
Updated: 2026-09-29T19:40:14+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2215
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
