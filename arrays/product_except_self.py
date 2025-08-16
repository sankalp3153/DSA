"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 852
Updated: 2025-08-16T20:17:50+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 852
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
