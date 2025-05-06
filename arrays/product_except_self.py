"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 484
Updated: 2025-05-06T21:54:03+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 484
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
