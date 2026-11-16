"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 2349
Updated: 2026-11-16T12:36:39+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2349
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
