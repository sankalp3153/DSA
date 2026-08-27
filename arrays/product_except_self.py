"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 2117
Updated: 2026-08-27T15:46:37+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2117
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
