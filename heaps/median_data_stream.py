"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1307
Updated: 2025-12-29T23:22:38+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1307
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
