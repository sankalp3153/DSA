"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1450
Updated: 2026-02-08T12:28:39+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1450
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
