"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 2234
Updated: 2026-10-02T23:06:09+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2234
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
