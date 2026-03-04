"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1542
Updated: 2026-03-04T23:22:35+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1542
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
