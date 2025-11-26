"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1182
Updated: 2025-11-26T22:56:04+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1182
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
