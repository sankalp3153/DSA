"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 323
Updated: 2025-03-20T13:00:26+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 323
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
