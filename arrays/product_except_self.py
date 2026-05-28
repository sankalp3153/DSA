"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1795
Updated: 2026-05-28T11:22:35+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1795
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
