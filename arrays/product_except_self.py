"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 2002
Updated: 2026-07-26T12:40:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2002
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
