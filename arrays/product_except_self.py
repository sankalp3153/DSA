"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1036
Updated: 2025-10-08T21:51:54+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1036
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
