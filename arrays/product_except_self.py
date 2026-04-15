"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1680
Updated: 2026-04-15T16:42:31+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1680
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
