"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1266
Updated: 2025-12-18T12:12:20+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1266
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
