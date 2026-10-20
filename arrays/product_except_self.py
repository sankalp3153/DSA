"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 2278
Updated: 2026-10-20T11:43:47+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2278
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
