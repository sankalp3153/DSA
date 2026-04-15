"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1682
Updated: 2026-04-15T18:18:18+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1682
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
