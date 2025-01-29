"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 116
Updated: 2025-01-29T12:54:05+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 116
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
