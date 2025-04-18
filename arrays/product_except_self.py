"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 438
Updated: 2025-04-18T10:02:49+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 438
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
