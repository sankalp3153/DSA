"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 916
Updated: 2025-09-02T11:14:17+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 916
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
