"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 870
Updated: 2025-08-20T23:08:18+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 870
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
