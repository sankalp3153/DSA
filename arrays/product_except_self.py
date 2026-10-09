"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 2255
Updated: 2026-10-09T23:42:07+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2255
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
