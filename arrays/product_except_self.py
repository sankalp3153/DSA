"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 737
Updated: 2025-07-20T13:03:27+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 737
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
