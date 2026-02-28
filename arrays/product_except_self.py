"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1519
Updated: 2026-02-28T12:41:44+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1519
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
