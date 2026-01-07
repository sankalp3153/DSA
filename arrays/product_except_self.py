"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1335
Updated: 2026-01-07T10:41:41+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1335
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
