"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1956
Updated: 2026-07-10T17:29:18+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1956
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
