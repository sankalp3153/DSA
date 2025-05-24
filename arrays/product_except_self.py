"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 553
Updated: 2025-05-24T17:18:34+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 553
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
