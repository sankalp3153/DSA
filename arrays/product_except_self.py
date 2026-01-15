"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1358
Updated: 2026-01-15T17:24:42+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1358
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
