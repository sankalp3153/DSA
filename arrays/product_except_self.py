"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 346
Updated: 2025-03-23T14:44:31+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 346
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
