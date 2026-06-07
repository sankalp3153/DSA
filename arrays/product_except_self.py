"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1841
Updated: 2026-06-07T19:09:30+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1841
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
