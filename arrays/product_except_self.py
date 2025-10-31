"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1105
Updated: 2025-10-31T20:09:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1105
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
