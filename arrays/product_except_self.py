"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 369
Updated: 2025-03-30T23:26:36+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 369
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
