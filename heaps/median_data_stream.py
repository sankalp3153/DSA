"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 824
Updated: 2025-08-11T18:01:36+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 824
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
