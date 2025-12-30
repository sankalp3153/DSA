"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1312
Updated: 2025-12-30T22:15:23+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1312
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
