"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 1128
Updated: 2025-11-10T18:48:07+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1128
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
