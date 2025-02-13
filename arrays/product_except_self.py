"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 185
Updated: 2025-02-13T16:30:09+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 185
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
