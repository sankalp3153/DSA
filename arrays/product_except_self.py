"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 760
Updated: 2025-07-25T21:05:45+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 760
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
