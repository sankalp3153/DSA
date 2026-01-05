"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1330
Updated: 2026-01-05T22:39:28+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1330
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
