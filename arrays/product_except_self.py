"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 139
Updated: 2025-02-01T18:03:34+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 139
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
