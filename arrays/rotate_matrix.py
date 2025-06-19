"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 647
Updated: 2025-06-19T11:38:25+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 647
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
