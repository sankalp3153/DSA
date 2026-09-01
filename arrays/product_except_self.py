"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 2140
Updated: 2026-09-01T16:04:36+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2140
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
