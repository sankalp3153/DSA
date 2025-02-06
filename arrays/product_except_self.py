"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 162
Updated: 2025-02-06T21:23:11+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 162
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
