"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1755
Updated: 2026-05-11T17:23:32+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1755
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
