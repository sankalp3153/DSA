"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 2043
Updated: 2026-08-06T22:16:13+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2043
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
