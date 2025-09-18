"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 967
Updated: 2025-09-18T17:34:38+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 967
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
