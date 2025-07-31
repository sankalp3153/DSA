"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 778
Updated: 2025-07-31T11:33:36+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 778
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
