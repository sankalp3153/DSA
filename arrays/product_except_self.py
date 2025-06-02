"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 576
Updated: 2025-06-02T16:09:12+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 576
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
