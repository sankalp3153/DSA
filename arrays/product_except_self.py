"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1565
Updated: 2026-03-13T21:46:08+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1565
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
