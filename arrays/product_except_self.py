"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 622
Updated: 2025-06-14T15:22:39+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 622
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
