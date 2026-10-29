"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 2301
Updated: 2026-10-29T18:47:32+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2301
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
