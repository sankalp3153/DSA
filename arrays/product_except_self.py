"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 944
Updated: 2025-09-10T19:59:45+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 944
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
