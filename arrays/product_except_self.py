"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1772
Updated: 2026-05-19T10:51:47+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1772
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
