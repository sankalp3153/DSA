"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 254
Updated: 2025-03-04T20:34:37+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 254
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
