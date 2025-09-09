"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 939
Updated: 2025-09-09T20:27:04+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 939
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
