"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 783
Updated: 2025-08-01T22:17:23+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 783
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
