"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1659
Updated: 2026-04-10T22:56:15+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1659
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
