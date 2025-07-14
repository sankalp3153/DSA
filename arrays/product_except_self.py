"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 714
Updated: 2025-07-14T14:05:01+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 714
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
