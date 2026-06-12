"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1864
Updated: 2026-06-12T10:05:06+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1864
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
