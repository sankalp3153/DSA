"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1404
Updated: 2026-01-29T18:42:17+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1404
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
