"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1013
Updated: 2025-09-30T15:35:35+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1013
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
