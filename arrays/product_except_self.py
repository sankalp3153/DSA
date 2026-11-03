"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 2324
Updated: 2026-11-03T19:44:09+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2324
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
