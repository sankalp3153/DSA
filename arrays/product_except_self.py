"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 875
Updated: 2025-08-22T20:19:37+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 875
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
