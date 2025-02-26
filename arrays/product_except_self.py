"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 231
Updated: 2025-02-26T11:39:43+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 231
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
