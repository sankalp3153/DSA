"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 898
Updated: 2025-08-29T10:32:22+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 898
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
