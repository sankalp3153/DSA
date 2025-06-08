"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 599
Updated: 2025-06-08T18:16:40+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 599
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
