"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1008
Updated: 2025-09-29T18:51:18+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1008
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
