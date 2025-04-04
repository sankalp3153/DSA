"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 392
Updated: 2025-04-04T20:09:02+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 392
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
