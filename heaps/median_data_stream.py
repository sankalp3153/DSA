"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 732
Updated: 2025-07-18T22:02:57+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 732
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
