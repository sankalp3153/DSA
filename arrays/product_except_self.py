"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 47
Updated: 2025-01-09T16:48:19+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 47
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
