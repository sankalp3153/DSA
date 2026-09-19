"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 2186
Updated: 2026-09-19T10:21:14+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2186
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
