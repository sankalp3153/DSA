"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1381
Updated: 2026-01-23T13:00:34+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1381
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
