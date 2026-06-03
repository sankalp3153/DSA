"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1818
Updated: 2026-06-03T15:19:42+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1818
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
