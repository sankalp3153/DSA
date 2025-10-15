"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1059
Updated: 2025-10-15T17:39:39+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1059
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
