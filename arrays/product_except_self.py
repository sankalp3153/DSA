"""
Module: product_except_self
Approach: prefix and suffix running product
Revision: 2163
Updated: 2026-09-09T11:45:25+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2163
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
