"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1445
Updated: 2026-02-07T15:20:06+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1445
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
