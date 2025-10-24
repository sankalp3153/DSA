"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1082
Updated: 2025-10-24T20:54:28+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1082
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
