"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1289
Updated: 2025-12-26T15:33:09+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1289
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
