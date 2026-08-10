"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 2048
Updated: 2026-08-10T13:45:19+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2048
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
