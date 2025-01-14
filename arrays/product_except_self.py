"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 70
Updated: 2025-01-14T17:53:56+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 70
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
