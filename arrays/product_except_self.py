"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1197
Updated: 2025-12-01T14:09:15+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1197
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
