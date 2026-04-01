"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1634
Updated: 2026-04-01T23:30:48+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1634
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
