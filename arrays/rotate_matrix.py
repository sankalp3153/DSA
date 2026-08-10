"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 2050
Updated: 2026-08-10T22:05:40+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2050
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
