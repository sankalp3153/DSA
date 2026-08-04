"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 2025
Updated: 2026-08-04T11:47:38+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2025
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
