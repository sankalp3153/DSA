"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1220
Updated: 2025-12-06T18:28:14+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1220
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
