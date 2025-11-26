"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1174
Updated: 2025-11-26T14:12:35+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1174
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
