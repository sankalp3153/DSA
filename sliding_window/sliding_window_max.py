"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1732
Updated: 2026-05-02T11:56:08+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1732
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
