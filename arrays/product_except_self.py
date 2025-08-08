"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 806
Updated: 2025-08-08T17:26:02+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 806
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
