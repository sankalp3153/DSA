"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 645
Updated: 2025-06-19T10:32:37+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 645
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
