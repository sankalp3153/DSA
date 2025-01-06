"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 24
Updated: 2025-01-06T17:37:50+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 24
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
