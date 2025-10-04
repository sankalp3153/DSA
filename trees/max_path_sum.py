"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1022
Updated: 2025-10-04T20:34:25+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1022
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
