"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1496
Updated: 2026-02-22T15:02:14+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1496
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
