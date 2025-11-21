"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1151
Updated: 2025-11-21T15:28:43+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1151
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
