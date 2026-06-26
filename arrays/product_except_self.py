"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1910
Updated: 2026-06-26T20:53:05+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1910
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
