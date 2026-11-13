"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 2347
Updated: 2026-11-13T15:01:37+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2347
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
