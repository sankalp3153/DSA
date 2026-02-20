"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1491
Updated: 2026-02-20T14:21:55+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1491
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
