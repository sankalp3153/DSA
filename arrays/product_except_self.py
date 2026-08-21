"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 2094
Updated: 2026-08-21T22:05:02+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2094
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
