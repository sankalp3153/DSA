"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 530
Updated: 2025-05-19T23:23:36+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 530
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
