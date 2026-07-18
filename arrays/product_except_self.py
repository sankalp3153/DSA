"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1979
Updated: 2026-07-18T13:49:55+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1979
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
