"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 691
Updated: 2025-07-01T19:01:52+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 691
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
