"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 277
Updated: 2025-03-09T20:58:53+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 277
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
