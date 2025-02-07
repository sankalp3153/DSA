"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 164
Updated: 2025-02-07T14:56:14+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 164
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
