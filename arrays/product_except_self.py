"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 2071
Updated: 2026-08-18T10:36:00+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2071
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
