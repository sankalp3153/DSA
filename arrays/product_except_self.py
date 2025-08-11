"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 829
Updated: 2025-08-11T22:57:12+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 829
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
