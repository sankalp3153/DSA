"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1427
Updated: 2026-02-03T13:38:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1427
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
