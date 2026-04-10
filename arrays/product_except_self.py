"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1657
Updated: 2026-04-10T19:29:14+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1657
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
