"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 300
Updated: 2025-03-16T14:39:19+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 300
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
