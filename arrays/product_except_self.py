"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 921
Updated: 2025-09-03T16:34:59+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 921
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
