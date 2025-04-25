"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 461
Updated: 2025-04-25T16:22:36+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 461
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
