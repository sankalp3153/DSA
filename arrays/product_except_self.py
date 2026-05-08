"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1749
Updated: 2026-05-08T19:22:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1749
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
