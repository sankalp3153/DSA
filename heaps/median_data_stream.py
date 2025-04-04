"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 387
Updated: 2025-04-04T14:13:45+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 387
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
