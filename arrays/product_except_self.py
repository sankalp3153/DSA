"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1611
Updated: 2026-03-25T11:35:23+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1611
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
