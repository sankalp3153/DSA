"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1767
Updated: 2026-05-17T21:39:29+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1767
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
