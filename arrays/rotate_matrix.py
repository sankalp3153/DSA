"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1245
Updated: 2025-12-13T12:59:49+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1245
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
