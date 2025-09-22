"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 985
Updated: 2025-09-22T10:36:34+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 985
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
