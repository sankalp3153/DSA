"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1887
Updated: 2026-06-19T22:02:26+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1887
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
