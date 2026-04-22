"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1703
Updated: 2026-04-22T10:12:53+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1703
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
