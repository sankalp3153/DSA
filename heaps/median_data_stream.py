"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 755
Updated: 2025-07-24T19:01:48+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 755
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
