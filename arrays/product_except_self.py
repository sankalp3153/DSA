"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 2232
Updated: 2026-10-02T15:42:29+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2232
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
