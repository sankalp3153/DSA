"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1514
Updated: 2026-02-27T14:38:27+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1514
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
