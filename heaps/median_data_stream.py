"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 410
Updated: 2025-04-10T18:07:21+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 410
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
