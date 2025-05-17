"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 525
Updated: 2025-05-17T15:49:06+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 525
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
