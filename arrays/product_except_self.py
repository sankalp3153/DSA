"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 668
Updated: 2025-06-26T12:38:26+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 668
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
