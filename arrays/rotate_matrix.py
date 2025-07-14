"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 716
Updated: 2025-07-14T16:02:19+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 716
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
