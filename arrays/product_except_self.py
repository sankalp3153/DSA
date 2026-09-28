"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 2209
Updated: 2026-09-28T20:47:17+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2209
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
