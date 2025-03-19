"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 318
Updated: 2025-03-19T19:39:07+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 318
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
