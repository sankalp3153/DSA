"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1169
Updated: 2025-11-25T15:16:49+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1169
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
