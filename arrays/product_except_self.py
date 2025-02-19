"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 208
Updated: 2025-02-19T15:07:08+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 208
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
