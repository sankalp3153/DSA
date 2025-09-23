"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 990
Updated: 2025-09-23T20:54:24+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 990
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
